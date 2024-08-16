# coding: utf-8
import json
import io
import xlsxwriter
from odoo import fields, models
from odoo.exceptions import ValidationError
from odoo.tools import date_utils


class ClassReportWizard(models.TransientModel):
    """This class report wizard"""

    _name = 'class.report.wizard'
    _description = 'Club Report Wizard'

    class_ids = fields.Many2many('student.class', string='Class')
    student_ids = fields.Many2many('student.registration', string='Student',
                                   domain="[ ('state', '=', 'registration')]")
    type = fields.Selection(
        string='Type',
        selection=[("class", "Class"), ("student", "Student")])

    def action_report_class(self):
        """This  will call report_action and return datas"""

        data = {
            'date': self.read()[0],
            'class_ids': self.class_ids.ids,
            'student_ids': self.student_ids.ids,
            'type': self.type
        }
        print('data', data)
        return self.env.ref(
            'school_management.action_class_report').report_action(
            None, data=data)

    def action_report_xlx_class(self):
        """ This is used to fetch data using query """
        query = """SELECT sl.name as class_name, sl.id as class_id, ss.name  as school,
                       sr.name AS department_name, 
                       st.first_name AS student_name,st.email as email,st.sequence as sequence, st.id as student_id
                        FROM student_class sl
                        Join res_company ss on sl.school_id = ss.id
                        JOIN student_department sr ON sr.id = sl.department_id
                        JOIN student_registration st ON st.student_class_id = sl.id """

        params = []

        if self.student_ids:

            print('condition')
            query += " AND st.id in %s "
            params.append(tuple(self.student_ids.ids))
            print(params)
            print(query)

        elif self.class_ids:
            query += """ AND st.student_class_id IN %s"""
            params.append(tuple(self.class_ids.ids))

        self.env.cr.execute(query, params)
        report = self.env.cr.dictfetchall()
        # print(report)
        if not report:
            print('no result')
            raise ValidationError("No related report found")

        data = {
            'result': report,
            'date': self.read()[0]
        }

        return {
            'type': 'ir.actions.report',
            'data': {'model': 'class.report.wizard',
                     'options': json.dumps(data,
                                           default=date_utils.json_default),
                     'output_format': 'xlsx',
                     'report_name': 'Class Excel Report',

                     },
            'report_type': 'xlsx',
        }

    def get_xlsx_report(self, data, response):

        report = data.get('result', [])
        result = data.get('date', [])
        print(report)
        student_ids = list(set(record['student_id'] for record in report))
        print(student_ids)
        class_ids = list(set(record['class_id'] for record in report))
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet()
        head = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '14px'})
        sub_head = workbook.add_format(
            {'font_size': '15px', 'align': 'center', 'font_color': '#333333'})
        txt = workbook.add_format({'font_size': '10px', 'align': 'center'})

        sheet.merge_range('B1:I3', 'CLASS REPORT', head)
        sheet.set_column('A:A', 15)
        sheet.set_column('B:B', 15)
        sheet.set_column('C:C', 15)
        sheet.set_column('D:D', 15)
        sheet.set_column('E:E', 15)
        sheet.set_column('F:F', 15)
        sheet.set_column('H:H', 15)
        sheet.set_column('G:G', 15)

        if result.get('type') == 'student':
            if len(student_ids) == 1:
                print('hiiiii')
                student_name = report[0].get('student_name')
                print(student_name)
                sheet.merge_range('A4:D4', 'Student: ' + student_name, sub_head)
                sheet.write('D7', 'SL NO', head)
                sheet.write('E7', 'R NO', head)
                sheet.write('F7', 'Class', head)
                sheet.write('G7', 'School', head)

                index = 1
                row = 7
                for record in report:
                    sheet.write(row, 3, index, txt)
                    sheet.write(row, 4, record.get('sequence', ''), txt)
                    sheet.write(row, 5, record.get('class_name', ''), txt)
                    sheet.write(row, 6, record.get('school', ''), txt)

                    row += 1
                    index += 1
            else:
                sheet.write('A7', 'SL.NO', head)
                sheet.write('B7', 'R.NO', head)
                sheet.write('C7', 'Student ', head)
                sheet.write('D7', 'Email ', head)
                sheet.write('E7', 'Class', head)
                sheet.write('F7', 'School', head)

                index = 1
                row = 7
                for record in report:
                    sheet.write(row, 0, index, txt)
                    sheet.write(row, 1, record.get('sequence', ''), txt)
                    sheet.write(row, 2, record.get('student_name', ''), txt)
                    sheet.write(row, 3, record.get('email', ''), txt)
                    sheet.write(row, 4, record.get('class_name', ''), txt)
                    sheet.write(row, 5, record.get('school', ''), txt)

                    row += 1
                    index += 1

        else:
            if len(class_ids) == 1:
                class_name = report[0].get('class_name')
                sheet.merge_range('A4:D4', 'Class: ' + class_name, sub_head)
                sheet.write('D7', 'SL NO', head)
                sheet.write('E7', 'R NO', head)
                sheet.write('F7', 'Student', head)
                sheet.write('G7', 'Email', head)
                sheet.write('H7', 'School', head)

                index = 1
                row = 7
                for record in report:
                    sheet.write(row, 3, index, txt)
                    sheet.write(row, 4, record.get('sequence', ''), txt)
                    sheet.write(row, 5, record.get('student_name', ''), txt)
                    sheet.write(row, 6, record.get('email', ''), txt)
                    sheet.write(row, 7, record.get('school', ''), txt)
                    row += 1
                    index += 1
            else:
                sheet.write('A7', 'SL.NO', head)
                sheet.write('B7', 'R.NO', head)
                sheet.write('C7', 'Student ', head)
                sheet.write('D7', 'Email ', head)
                sheet.write('E7', 'Class', head)
                sheet.write('F7', 'School', head)

                index = 1
                row = 7
                for record in report:
                    sheet.write(row, 0, index, txt)
                    sheet.write(row, 1, record.get('sequence', ''), txt)
                    sheet.write(row, 2, record.get('student_name', ''), txt)
                    sheet.write(row, 3, record.get('email', ''), txt)
                    sheet.write(row, 4, record.get('class_name', ''), txt)
                    sheet.write(row, 5, record.get('school', ''), txt)

                    row += 1
                    index += 1

        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()
