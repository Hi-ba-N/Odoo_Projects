# coding: utf-8
from odoo import fields, models


class ClubReportWizard(models.TransientModel):
    _name = 'club.report.wizard'
    _description = 'Club Report Wizard'

    student_ids = fields.Many2many('student.registration', string='Student')

    def action_report_club(self):

        data = {
            'date': self.read()[0],
            'student_ids': self.student_ids.ids,

        }
        print(data)
        return self.env.ref(
            'school_management.action_club_report').report_action(
            None, data=data)
