# coding: utf-8
from odoo import fields, models


class ClubReportWizard(models.TransientModel):
    """This club report wizard"""
    _name = 'club.report.wizard'
    _description = 'Club Report Wizard'

    type = fields.Selection(
        string='Type',
        selection=[("club", "Club"), ("student", "Student")])
    student_ids = fields.Many2many('student.registration', string='Student', domain="[ ('state', '=', 'registration')]")
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
