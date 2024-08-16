# coding: utf-8
import json
import io
import xlsxwriter
from odoo import fields, models
from odoo.exceptions import ValidationError
from odoo.tools import date_utils


class ClubReportWizard(models.TransientModel):
    """This club report wizard"""
    _name = 'club.report.wizard'
    _description = 'Club Report Wizard'

    type = fields.Selection(
        string='Type',
        selection=[("club", "Club"), ("student", "Student")])
    student_ids = fields.Many2many('student.registration', string='Student',
                                   domain="[ ('state', '=', 'registration')]")
    club_ids = fields.Many2many('student.club', string='Club')

    def action_report_club(self):
        """This  will call report_action and return datas"""

        data = {
            'date': self.read()[0],
            'student_ids': self.student_ids.ids,
            'club_ids': self.club_ids.ids
        }
        print(data)
        return self.env.ref(
            'school_management.action_club_report').report_action(
            None, data=data)

    def action_report_xlx_club(self):
        """ This is used to fetch data using query """
        query = """SELECT sr.first_name AS student_name, sr.id as student_id ,
        sr.sequence as reg_no, sr.email as email,
            sc.name AS club_name,sc.id AS club_id, sc.description as desc 
                            FROM student_registration sr
                            JOIN student_club_student_registration_rel sp ON sr.id = student_registration_id
                            JOIN student_club sc ON sc.id = student_club_id """

        params = []

        if self.student_ids:
            print('student select')
            query += "  AND sr.id IN %s"
            params.append(tuple(self.student_ids.ids))

        elif self.club_ids:
            query += "  AND sc.id IN %s"
            params.append(tuple(self.club_ids.ids))

        self.env.cr.execute(query, params)

        report = self.env.cr.dictfetchall()
        if not report:
            print('no result')
            raise ValidationError("No related report found")

        data = {
            'result': report
        }

        return {
            'type': 'ir.actions.report',
            'data': {'model': 'club.report.wizard',
                     'options': json.dumps(data,
                                           default=date_utils.json_default),
                     'output_format': 'xlsx',
                     'report_name': 'Club Excel Report',

                     },
            'report_type': 'xlsx',
        }

    def get_xlsx_report(self, data, response):
        report = data.get('result', [])
        print(report)
        student_ids = list(set(record['student_id'] for record in report))
        club_ids = list(set(record['club_id'] for record in report))
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet()
        head = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '14px'})
        sub_head = workbook.add_format(
            {'font_size': '15px', 'align': 'center', 'font_color': '#333333'})

        txt = workbook.add_format({'font_size': '10px', 'align': 'center'})

        sheet.merge_range('B1:I3', 'CLUB REPORT', head)
        sheet.set_column('A:A', 15)
        sheet.set_column('B:B', 15)
        sheet.set_column('C:C', 15)
        sheet.set_column('D:D', 15)
        sheet.set_column('E:E', 15)
        sheet.set_column('F:F', 15)
        sheet.set_column('H:H', 15)
        sheet.set_column('G:G', 15)

        if len(student_ids) == 1:
            print('djjd')
            student_name = report[0].get('student_name')
            sheet.merge_range('A4:D4', 'STUDENT: ' + student_name, sub_head)
            sheet.write('D7', 'SL NO', head)
            sheet.write('E7', 'Club', head)
            sheet.write('F7', 'Description', head)

            index = 1
            row = 7
            for record in report:
                sheet.write(row, 3, index, txt)
                sheet.write(row, 4, str(record.get('club_name', '')), txt)
                sheet.write(row, 5, str(record.get('desc', '')), txt)
                row += 1
                index += 1

        elif len(club_ids) == 1:
            club_name = report[0].get('club_name')
            sheet.merge_range('A4:D4', 'CLUB: ' + club_name, sub_head)
            sheet.write('D7', 'SL NO', head)
            sheet.write('E7', 'R No', head)
            sheet.write('F7', 'Student', head)
            sheet.write('G7', 'Email', head)

            index = 1
            row = 7
            for record in report:
                sheet.write(row, 3, index, txt)
                sheet.write(row, 4, str(record.get('reg_no', '')), txt)
                sheet.write(row, 5, str(record.get('student_name', '')), txt)
                sheet.write(row, 6, str(record.get('email', '')), txt)

                row += 1
                index += 1

        else:
            sheet.write('A7', 'SL.NO', head)
            sheet.write('B7', 'R NO ', head)
            sheet.write('C7', 'Student ', head)
            sheet.write('D7', 'Email', head)
            sheet.write('E7', 'Club', head)

            index = 1
            row = 7
            for record in report:
                sheet.write(row, 0, index, txt)
                sheet.write(row, 1, str(record.get('reg_no', '')), txt)
                sheet.write(row, 2, str(record.get('student_name', '')), txt)
                sheet.write(row, 3, str(record.get('email', '')), txt)
                sheet.write(row, 4, str(record.get('club_name', '')), txt)

                row += 1
                index += 1

        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()
