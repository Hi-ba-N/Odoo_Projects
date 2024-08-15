# coding: utf-8
import json
import io
import xlsxwriter
<<<<<<< HEAD
from datetime import date

from odoo import fields, models
=======
from datetime import timedelta, date

from odoo import api, fields, models
>>>>>>> d6f0197172a30655fb4f75c274aba406265d547e
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
<<<<<<< HEAD
        query = """SELECT sl.start_date, sl.end_date , sl.total_days, sl.reason, sr.first_name AS student_name,
        sr.sequence AS sequence,sr.id as student_id,sr.email as email, sc.name AS class_name, sc.id as class_id FROM student_leave sl 
        JOIN student_registration sr ON sr.id = sl.student_id JOIN student_class sc ON sc.id = sr.student_class_id"""
=======
        query = """SELECT sl.start_date, sl.end_date , sl.total_days, sl.reason,
                                                 sr.first_name AS student_name,sr.sequence AS sequence,sr.id as student_id,sc.name AS class_name, sc.id as class_id
                                          FROM student_leave sl
                                          JOIN student_registration sr ON sr.id = sl.student_id
                                          JOIN student_class sc ON sc.id = sr.student_class_id
                                          """
>>>>>>> d6f0197172a30655fb4f75c274aba406265d547e

        params = []

        if self.class_ids.ids:
            query += " AND sr.student_class_id IN %s"
            params.append(tuple(self.class_ids.ids))
            print(query)
<<<<<<< HEAD
        elif self.student_ids.ids:
            query += " AND sl.student_id IN %s"
            params.append(tuple(self.student_ids.ids))
=======
        elif self.student_ids:
            query += " AND sl.student_id IN %s"
            params.append(tuple(self.student_ids))
>>>>>>> d6f0197172a30655fb4f75c274aba406265d547e
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
<<<<<<< HEAD

        if not report:
            print('no result')
            raise ValidationError("No related report found")

        data = {
            'result': report
        }
=======
        if not report:
            print('no result')
            raise ValidationError("No related report found")
        print(report)
>>>>>>> d6f0197172a30655fb4f75c274aba406265d547e

        return {
            'type': 'ir.actions.report',
            'data': {'model': 'leave.report.wizard',
<<<<<<< HEAD
                     'options': json.dumps(data,
                                           default=date_utils.json_default),
                     'output_format': 'xlsx',
                     'report_name': 'Leave Excel Report',

=======
                     'options': json.dumps(report,
                                           default=date_utils.json_default),
                     'output_format': 'xlsx',
                     'report_name': 'Leave Excel Report',
>>>>>>> d6f0197172a30655fb4f75c274aba406265d547e
                     },
            'report_type': 'xlsx',
        }

    def get_xlsx_report(self, data, response):
<<<<<<< HEAD
        report = data.get('result', [])
        print(report)
        student_ids = list(set(record['student_id'] for record in report))
        print(student_ids)
        class_ids = list(set(record['student_id'] for record in report))
        print('hello', report)
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet()
        head = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '14px'})

        txt = workbook.add_format({'font_size': '10px', 'align': 'center'})

        sheet.merge_range('B1:I3', 'LEAVE REPORT', head)
        sheet.set_column('A:A', 15)
        sheet.set_column('B:B', 15)
        sheet.set_column('C:C', 15)
        sheet.set_column('D:D', 15)
        sheet.set_column('E:E', 15)
        sheet.set_column('F:F', 15)
        sheet.set_column('H:H', 15)
        sheet.set_column('G:G', 15)

        if len(student_ids) == 1 :
            print('djjd')
            student_name = report[0].get('student_name')
            class_name = report[0].get('class_name')
            print(student_name)
            sheet.merge_range('A4:D4', 'Student: ' + student_name, txt)
            sheet.merge_range('A5:D5', 'Class: ' + class_name, txt)
            sheet.write('D7', 'SL NO', head)
            sheet.write('E7', 'Start Date', head)
            sheet.write('F7', 'End Date', head)
            sheet.write('G7', 'Total', head)
            sheet.write('H7', 'Reason', head)

            index = 1
            row = 7
            for record in report:
                sheet.write(row, 3, index, txt)
                sheet.write(row, 4, str(record.get('start_date', '')), txt)
                sheet.write(row, 5, str(record.get('end_date', '')), txt)
                sheet.write(row, 6, record.get('total_days', ''), txt)
                sheet.write(row, 7, record.get('reason', ''), txt)
                row += 1
                index += 1

        elif len(class_ids) == 1:
            print('3')
            class_name = report[0].get('class_name')
            sheet.merge_range('A5:D5', 'Class: ' + class_name, txt)
            sheet.write('A7', 'R.NO', head)
            sheet.write('B7', 'Student ', head)
            sheet.write('C7', 'Start Date', head)
            sheet.write('D7', 'End Date', head)
            sheet.write('E7', 'Total', head)
            sheet.write('F7', 'Reason', head)
            row = 7
            for record in report:
                sheet.write(row, 0, str(record.get('sequence', '')), txt)
                sheet.write(row, 1, str(record.get('student_name', '')), txt)
                sheet.write(row, 2, str(record.get('start_date', '')), txt)
                sheet.write(row, 3, str(record.get('end_date', '')), txt)
                sheet.write(row, 4, record.get('total_days', ''), txt)
                sheet.write(row, 5, record.get('reason', ''), txt)
                row += 1
        else:
            print('2')
            # sheet.write('A7', 'SL NO', head)

            sheet.write('A7', 'R.NO', head)
            sheet.write('B7', 'Student ', head)
            sheet.write('C7', 'Class ', head)
            sheet.write('D7', 'Start Date', head)
            sheet.write('E7', 'End Date', head)
            sheet.write('F7', 'Total', head)
            sheet.write('G7', 'Reason', head)

            row = 7
            for record in report:
                # sheet.write(row, 0, index, txt)
                sheet.write(row, 0, str(record.get('sequence', '')), txt)
                sheet.write(row, 1, record.get('student_name', ''), txt)
                sheet.write(row, 2, record.get('class_name', ''), txt)
                sheet.write(row, 3, str(record.get('start_date', '')), txt)
                sheet.write(row, 4, str(record.get('end_date', '')), txt)
                sheet.write(row, 5, record.get('total_days', ''), txt)
                sheet.write(row, 6, record.get('reason', ''), txt)
                row += 1

=======
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
>>>>>>> d6f0197172a30655fb4f75c274aba406265d547e
        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()
