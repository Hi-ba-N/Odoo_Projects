# coding: utf-8
from odoo import fields, models


class EventReportWizard(models.TransientModel):
    """This event report wizard"""
    _name = 'event.report.wizard'
    _description = 'Event Report Wizard'

    frequency = fields.Selection(
        string='Frequency',
        selection=[("day", "Daily"), ("week", "Weekly"), ('month', 'Monthly'),
                   ('custom', 'Custom')])
    club_ids = fields.Many2many('student.club', string='Club')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')

    def action_report_event(self):
        """This  will call report_action"""
        data = {
            'date': self.read()[0],
            'club_ids': self.club_ids.ids,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'frequency': self.frequency

        }
        print(data)
        return self.env.ref(
            'school_management.action_event_report').report_action(
            None, data=data)
