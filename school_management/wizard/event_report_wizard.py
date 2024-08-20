# coding: utf-8
from datetime import date
import json
import io
import xlsxwriter
from odoo import fields, models
from odoo.exceptions import ValidationError
from odoo.tools import date_utils


class EventReportWizard(models.TransientModel):
    """This event report wizard"""
    _name = 'event.report.wizard'
    _description = 'Event Report Wizard'

    frequency = fields.Selection(
        string='Frequency',
        selection=[("day", "Daily"), ("week", "Weekly"), ('month', 'Monthly'),
                   ('custom', 'Custom')])
    club_ids = fields.Many2many('student.club', string='Club')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')

    def action_report_event(self):
        """This  will call report_action"""
        data = {
            'date': self.read()[0],
            'club_ids': self.club_ids.ids,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'frequency': self.frequency

        }
        print(data)
        return self.env.ref(
            'school_management.action_event_report').report_action(
            None, data=data)

    def action_report_xlx_event(self):
        """ Fetching data from database based on condition"""
        query = """SELECT sl.id, sl.name, sl.start_date,sl.end_date, sl.venue, 
                             sr.name AS club_name ,sr.id as club_id          
                            FROM student_event sl
                            JOIN student_club sr ON sr.id = sl.club_id
                                          """

        params = []

        if self.club_ids.ids:
            query += " AND sl.club_id IN %s"
            params.append(tuple(self.club_ids.ids))
        if self.frequency == 'day':
            query += " where extract (day from start_date)= extract(day from current_date)"
        elif self.frequency == 'week':
            query += " where extract (week from start_date)= extract(week from current_date)"
        elif self.frequency == 'month':
            query += " where extract (month from start_date)= extract(month from current_date)"
        elif self.start_date and self.end_date:
            query += " where start_date >= '%s' and end_date >= '%s'" % (
                self.start_date, self.end_date)
        elif self.start_date and not self.end_date:
            query += "where start_date >= '%s' and end_date <= '%s'" % (
                self.start_date, date.today())
            print(query)
        elif self.end_date and not self.end_date:
            query += "where end_date <= '%s'" % self.end_date

        self.env.cr.execute(query, params)
        report = self.env.cr.dictfetchall()

        if not report:
            print('no result')
            raise ValidationError("No related report found")

        data = {
            'result': report,

        }

        return {
            'type': 'ir.actions.report',
            'data': {'model': 'event.report.wizard',
                     'options': json.dumps(data,
                                           default=date_utils.json_default),
                     'output_format': 'xlsx',
                     'report_name': 'Event Excel Report',

                     },
            'report_type': 'xlsx',
        }

    def get_xlsx_report(self, data, response):
        report = data.get('result', [])
        # result = data.get('date', [])
        print('rep', report)
        club_ids = list(set(record['club_id'] for record in report))
        print(club_ids)
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet()
        head = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '14px'})

        txt = workbook.add_format({'font_size': '10px', 'align': 'center'})
        sub_head = workbook.add_format(
            {'font_size': '12px', 'align': 'center', 'font_color': '#333333'})

        sheet.merge_range('B1:I3', 'EVENT REPORT', head)
        sheet.set_column('A:H', 25)

        if len(club_ids) == 1:
            print('djjd')
            club_name = report[0].get('club_name')
            print(club_name)
            sheet.merge_range('A5:E5', 'Club: ' + club_name, sub_head)
            sheet.write('A8', 'SL NO', head)
            sheet.write('B8', 'Event', head)
            sheet.write('C8', 'Start Date', head)
            sheet.write('D8', 'End Date', head)
            sheet.write('E8', 'Venue', head)

            index = 1
            row = 8
            for record in report:
                sheet.write(row, 0, index, txt)
                sheet.write(row, 1, record.get('name', ''), txt)
                sheet.write(row, 2, str(record.get('start_date', '')), txt)
                sheet.write(row, 3, str(record.get('end_date', '')), txt)
                sheet.write(row, 4, record.get('venue', ''), txt)

                row += 1
                index += 1
        elif len(club_ids) > 1:
            print('gggg')
            sheet.write('A5', 'SL NO', head)
            sheet.write('B5', 'Club', head)
            sheet.write('C5', 'Event', head)
            sheet.write('D5', 'Start Date', head)
            sheet.write('E5', 'End Date', head)
            sheet.write('F5', 'Venue', head)

            index = 1
            row = 5
            for record in report:
                sheet.write(row, 0, index, txt)
                sheet.write(row, 1, record.get('club_name', ''), txt)
                sheet.write(row, 2, record.get('name', ''), txt)
                sheet.write(row, 3, str(record.get('start_date', '')), txt)
                sheet.write(row, 4, str(record.get('end_date', '')), txt)
                sheet.write(row, 5, record.get('venue', ''), txt)
                row += 1
                index += 1

        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()
