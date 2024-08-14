# coding: utf-8
import json
import io
import xlsxwriter
from datetime import timedelta, date

from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools import date_utils


class LeaveReportWizard(models.TransientModel):
    """This leave report wizard"""
    _name = 'leave.report.wizard'
    _description = 'Leave Report Wizard'

    frequency = fields.Selection(
        string='Frequency',
        selection=[("day", "Daily"), ("week", "Weekly"), ('month', 'Monthly'),
                   ('custom', 'Custom')])
    type = fields.Selection(
        string='Type',
        selection=[("class", "Class"), ("student", "Student")])
    class_ids = fields.Many2many('student.class', string='Class')
    student_ids = fields.Many2many('student.registration', string='Student', domain="[ ('state', '=', 'registration')]")
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')

    def action_report_leave(self):
        """This  will call report_action and return datas"""

        data = {
            'date': self.read()[0],
            'class_ids': self.class_ids.ids,
            'student_ids': self.student_ids.ids,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'frequency': self.frequency,
            'type': self.type
        }

        print(data)
        return self.env.ref(
            'school_management.action_leave_report').report_action(
            None, data=data)

    def action_report_xlx_leave(self):
        query = """SELECT sl.start_date, sl.end_date , sl.total_days, sl.reason,
                                                 sr.first_name AS student_name,sr.sequence AS sequence,sr.id as student_id,sc.name AS class_name, sc.id as class_id
                                          FROM student_leave sl
                                          JOIN student_registration sr ON sr.id = sl.student_id
                                          JOIN student_class sc ON sc.id = sr.student_class_id
                                          """

        params = []

        if self.class_ids.ids:
            query += " AND sr.student_class_id IN %s"
            params.append(tuple(self.class_ids.ids))
            print(query)
        elif self.student_ids:
            query += " AND sl.student_id IN %s"
            params.append(tuple(self.student_ids))
        if self.frequency == 'day':
            query += " where extract (day from start_date)= extract(day from current_date)"
        elif self.frequency == 'week':
            query += " where extract (week from start_date)= extract(week from current_date)"
        elif self.frequency == 'month':
            query += " where extract (month from start_date)= extract(month from current_date)"
        elif self.end_date < self.start_date:
            print('choose valid')
            raise ValidationError(
                'Choose valid date')
        elif self.start_date and self.end_date:
            query += " where start_date >= '%s' and end_date >= '%s'" % (
                self.start_date, self.end_date)
        elif self.start_date and not self.end_date:
            query += "where start_date >= '%s' and end_date <= '%s'" % (
                self.start_date, date.today())
            print(query)
        elif self.end_date and not self.start_date:
            query += "where end_date <= '%s'" % self.end_date

        self.env.cr.execute(query, params)
        report = self.env.cr.dictfetchall()
        if not report:
            print('no result')
            raise ValidationError("No related report found")
        print(report)

        return {
            'type': 'ir.actions.report',
            'data': {'model': 'leave.report.wizard',
                     'options': json.dumps(report,
                                           default=date_utils.json_default),
                     'output_format': 'xlsx',
                     'report_name': 'Leave Excel Report',
                     },
            'report_type': 'xlsx',
        }

    def get_xlsx_report(self, data, response):
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format(
            {'font_size': '12px', 'align': 'center'})
        head = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '20px'})
        txt = workbook.add_format({'font_size': '10px', 'align': 'center'})
        sheet.merge_range('B2:I3', 'LEAVE REPORT', head)
        # sheet.merge_range('A4:B4', 'Customer:', cell_format)
        # sheet.merge_range('C4:D4', data['customer'], txt)
        # sheet.merge_range('A5:B5', 'Products', cell_format)
        # for i, product in enumerate(data['products'],
        #                             start=5):  # Start at row 6 for products
        #     sheet.merge_range(f'C{i}:D{i}', product, txt)
        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()
