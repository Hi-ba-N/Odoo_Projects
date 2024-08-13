# coding: utf-8
from odoo import fields, models


class ClassReportWizard(models.TransientModel):
    """This class report wizard"""

    _name = 'class.report.wizard'
    _description = 'Club Report Wizard'

    department_id = fields.Many2one('student.department', string='Department')
    class_ids = fields.Many2many('student.class', string='Class')

    def action_report_class(self):
        """This  will call report_action and return datas"""

        data = {
            'date': self.read()[0],
            'department_id': self.department_id.ids,
            'class_ids': self.class_ids.ids
        }
        print('data', data)
        return self.env.ref(
            'school_management.action_class_report').report_action(
            None, data=data)
