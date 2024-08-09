# coding: utf-8
from datetime import timedelta

from odoo import api, fields, models


class LeaveReportWizard(models.TransientModel):
    _name = 'leave.report.wizard'
    _description = 'Leave Report Wizard'

    frequency = fields.Selection(
        string='Frequency',
        selection=[("day", "Daily"), ("week", "Weekly"), ('month', 'Monthly'),
                   ('custom', 'Custom')])
    type = fields.Selection(
        string='Type',
        selection=[("class", "Class"), ("student", "Student")])
    class_ids = fields.Many2many('student.class', string='Class')
    student_ids = fields.Many2many('student.registration', string='Student')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')

    def action_report_leave(self):
        """This  will call report_action"""

        data = {
            'date': self.read()[0],
            'class_ids': self.class_ids.ids,
            'student_ids': self.student_ids.ids,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'frequency': self.frequency
        }

        print(data)
        return self.env.ref(
            'school_management.action_leave_report').report_action(
            None, data=data)
