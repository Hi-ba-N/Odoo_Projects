# coding: utf-8
from odoo import fields, models


class ClassReportWizard(models.TransientModel):
    _name = 'class.report.wizard'
    _description = 'Club Report Wizard'

    department_id = fields.Many2one('student.department', string='Department')

    def action_report_class(self):

        data = {
            'date': self.read()[0],
            'department_id': self.department_id.ids,
        }
        print('data', data)
        return self.env.ref(
            'school_management.action_class_report').report_action(
            None, data=data)
