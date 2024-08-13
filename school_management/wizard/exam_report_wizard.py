# coding: utf-8
from odoo import fields, models


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
        selection=[("class", "Class"), ("student", "Student")])

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
