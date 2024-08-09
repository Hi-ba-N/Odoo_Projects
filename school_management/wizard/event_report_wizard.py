# coding: utf-8
from odoo import fields, models


class EventReportWizard(models.TransientModel):
    _name = 'event.report.wizard'
    _description = 'Event Report Wizard'

    frequency = fields.Selection(
        string='Frequency',
        selection=[("day", "Daily"), ("week", "Weekly"), ('month', 'Monthly')])
    club_ids = fields.Many2many('student.club', string='Club')

    def action_report_event(self):

        data = {
            'date': self.read()[0],
            'club_ids': self.club_ids.ids,

        }
        print(data)
        return self.env.ref(
            'school_management.action_event_report').report_action(
            None, data=data)
