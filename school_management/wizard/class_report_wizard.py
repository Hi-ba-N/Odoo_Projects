# coding: utf-8
from odoo import fields, models


class ClassReportWizard(models.TransientModel):
    """This class report wizard"""

    _name = 'class.report.wizard'
    _description = 'Club Report Wizard'

    class_ids = fields.Many2many('student.class', string='Class')
    student_ids = fields.Many2many('student.registration', string='Student',domain="[ ('state', '=', 'registration')]")
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
