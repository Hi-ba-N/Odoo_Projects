# coding: utf-8
import json
import io
import xlsxwriter
from odoo import fields, models
from odoo.exceptions import ValidationError
from odoo.tools import date_utils


class ExamReportWizard(models.TransientModel):
    """This exam report wizard"""

    _name = 'exam.report.wizard'
    _description = 'Exam Report Wizard'

    student_ids = fields.Many2many('student.registration', string='Student',
                                   domain="[('state', '=', 'registration')]")
    class_ids = fields.Many2many('student.class', 'Class')
    exam_ids = fields.Many2many('student.exams', 'Exam')
    type = fields.Selection(
        string='Type',
        selection=[("class", "Class"), ("student", "Student"),
                   ('exam', 'Exam')])

    def action_report_exam(self):
        """This  will call report_action and return datas"""

        data = {
            'date': self.read()[0],
            'student_ids': self.student_ids.ids,
            'class_ids': self.class_ids.ids,
            'exam_ids': self.exam_ids.ids,
            'type': self.type
        }
        print('data', data)
        return self.env.ref(
            'school_management.action_exam_report').report_action(
            None, data=data)

    def action_report_xlx_exam(self):
        query = """SELECT se.name as exam_name, sc.name as class_name, ss.name as subject_name , 
                                      sr.first_name as student_name, sr.id as student_id ,
                                      sr.sequence as sequence,
                                      sr.email as email,
                                      sc.id  as class_id,
                                      se.id as exam_id
                                      FROM student_exams se
                                      JOIN student_class sc ON se.class_id = sc.id
	                                  JOIN student_registration sr ON sr.student_class_id = sc.id
                                      JOIN student_paper sp ON sp.exam_id = se.id
                                      JOIN student_subject ss ON sp.subject_id = ss.id"""

        params = []

        if self.student_ids:
            query += """  AND  sr.id IN %s """

            params.append(tuple(self.student_ids.ids))
            print(tuple(params))

        elif self.class_ids:
            query += """ AND sc.id IN %s """
            params.append(tuple(self.class_ids.ids))

        elif self.exam_ids:
            query += """ AND se.id IN %s """

            params.append(tuple(self.exam_ids.ids))

        self.env.cr.execute(query, params)
        report = self.env.cr.dictfetchall()
        if not report:
            raise ValidationError("No related report found")

        data = {
            'result': report,
            'date': self.read()[0]
        }

        return {
            'type': 'ir.actions.report',
            'data': {'model': 'exam.report.wizard',
                     'options': json.dumps(data,
                                           default=date_utils.json_default),
                     'output_format': 'xlsx',
                     'report_name': 'Exam Excel Report',

                     },
            'report_type': 'xlsx',
        }

    def get_xlsx_report(self, data, response):
        report = data.get('result', [])
        result = data.get('date', [])
        print(report)
        student_ids = list(set(record['student_id'] for record in report))
        class_ids = list(set(record['class_id'] for record in report))
        exam_ids = list(set(record['exam_id'] for record in report))
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet()
        head = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '14px'})

        txt = workbook.add_format({'font_size': '10px', 'align': 'center'})
        sub_head = workbook.add_format(
            {'font_size': '12px', 'align': 'center', 'font_color': '#333333'})

        sheet.merge_range('B1:I3', 'EXAM REPORT', head)
        sheet.set_column('A:G', 20)
        if result.get('type') == 'student':
            if len(student_ids) == 1:
                print('stddd')
                student_name = report[0].get('student_name')
                class_name = report[0].get('class_name')
                print(student_name)
                sheet.merge_range('A4:D4', 'Student:  ' + student_name,
                                  sub_head)
                sheet.merge_range('A5:D5', 'Class:  ' + class_name, sub_head)
                sheet.write('A8', 'SL NO', head)
                sheet.write('B8', 'Exam', head)
                sheet.write('C8', 'Subject', head)

                index = 1
                row = 8
                for record in report:
                    sheet.write(row, 0, index, txt)
                    sheet.write(row, 1, record.get('exam_name', ''), txt)
                    sheet.write(row, 2, record.get('subject_name', ''), txt)
                    row += 1
                    index += 1

            else:
                print('first else')
                sheet.write('A7', 'SL.NO', head)
                sheet.write('B7', 'R.NO', head)
                sheet.write('C7', 'Student ', head)
                sheet.write('D7', 'Email ', head)
                sheet.write('E7', 'Class ', head)
                sheet.write('F7', 'Exam', head)
                index = 1
                row = 7
                for record in report:
                    sheet.write(row, 0, index, txt)
                    sheet.write(row, 1, record.get('sequence', ''), txt)
                    sheet.write(row, 2, record.get('student_name', ''), txt)
                    sheet.write(row, 3, record.get('email', ''), txt)
                    sheet.write(row, 4, record.get('class_name', ''), txt)
                    sheet.write(row, 5, record.get('exam_name', ''), txt)

                    row += 1
                    index += 1

        elif result.get('type') == 'class':
            if len(class_ids) == 1:
                print('class')
                class_name = report[0].get('class_name')
                sheet.merge_range('A5:D5', 'Class: ' + class_name, sub_head)
                sheet.write('A7', 'SL.NO', head)
                sheet.write('B7', 'R.NO', head)
                sheet.write('C7', 'Student ', head)
                sheet.write('D7', 'Email', head)
                sheet.write('E7', 'Exam', head)

                index = 1
                row = 7
                for record in report:
                    sheet.write(row, 0, index, txt)
                    sheet.write(row, 1, record.get('sequence', ''), txt)
                    sheet.write(row, 2, record.get('student_name', ''), txt)
                    sheet.write(row, 3, record.get('email', ''), txt)
                    sheet.write(row, 4, record.get('exam_name', ''), txt)

                    row += 1
                    index += 1
            else:
                print('second else')
                sheet.write('A7', 'SL.NO', head)
                sheet.write('B7', 'R.NO', head)
                sheet.write('C7', 'Student ', head)
                sheet.write('D7', 'Email ', head)
                sheet.write('E7', 'Class ', head)
                sheet.write('F7', 'Exam', head)
                index = 1
                row = 7
                for record in report:
                    sheet.write(row, 0, index, txt)
                    sheet.write(row, 1, record.get('sequence', ''), txt)
                    sheet.write(row, 2, record.get('student_name', ''), txt)
                    sheet.write(row, 3, record.get('email', ''), txt)
                    sheet.write(row, 4, record.get('class_name', ''), txt)
                    sheet.write(row, 5, record.get('exam_name', ''), txt)

                    row += 1
                    index += 1
        else:
            if len(exam_ids) == 1:
                print('exaaam')
                exam_name = report[0].get('exam_name')
                print(exam_name)
                sheet.merge_range('A5:D5', 'Exam: ' + exam_name, sub_head)
                sheet.write('A7', 'SL.NO', head)
                sheet.write('B7', 'Class', head)
                sheet.write('C7', 'Paper ', head)
                index = 1
                row = 7
                for record in report:
                    sheet.write(row, 0, index, txt)
                    sheet.write(row, 1, record.get('class_name', ''), txt)
                    sheet.write(row, 2, record.get('subject_name', ''), txt)
                    row += 1
                    index += 1
            else:
                sheet.write('A7', 'SL.NO', head)
                sheet.write('B7', 'R.NO', head)
                sheet.write('C7', 'Student ', head)
                sheet.write('D7', 'Email ', head)
                sheet.write('E7', 'Class ', head)
                sheet.write('F7', 'Exam', head)
                index = 1
                row = 7
                for record in report:
                    sheet.write(row, 0, index, txt)
                    sheet.write(row, 1, record.get('sequence', ''), txt)
                    sheet.write(row, 2, record.get('student_name', ''), txt)
                    sheet.write(row, 3, record.get('email', ''), txt)
                    sheet.write(row, 4, record.get('class_name', ''), txt)
                    sheet.write(row, 5, record.get('exam_name', ''), txt)

                    row += 1
                    index += 1

        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()
