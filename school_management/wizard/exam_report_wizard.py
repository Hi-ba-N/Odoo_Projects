# coding: utf-8
from odoo import fields, models


class ExamReportWizard(models.TransientModel):
    _name = 'exam.report.wizard'
    _description = 'Exam Report Wizard'

    student_ids = fields.Many2many('student.registration', string='Student')

    def action_report_exam(self):

        data = {
            'date': self.read()[0],
            'student_ids': self.student_ids.ids,
        }
        print('data', data)
        return self.env.ref(
            'school_management.action_exam_report').report_action(
            None, data=data)
