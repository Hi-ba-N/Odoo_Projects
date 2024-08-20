# coding: utf-8
from datetime import date, datetime, timedelta
from email.policy import default

from odoo import api, fields, models, exceptions
from odoo.fields import Date


class StudentEvent(models.Model):
    """This is used for student Event"""
    _name = "student.event"
    _description = "Event"
    _inherit = 'mail.thread'

    name = fields.Char(string="Name", required=True)
    description = fields.Html("Description")
    start_date = fields.Date(" Start Date", required=True)
    end_date = fields.Date("End Date", required=True)
    venue = fields.Char("Venue")
    image = fields.Binary()
    club_id = fields.Many2one('student.club', string="Club")
    active = fields.Boolean(default=True)
    state = fields.Selection(selection=[
        ('new', 'New'),
        ('booked', 'Booked'),
        ('cancelled', 'Cancelled')

    ], string='Status', required=True,
        default='new')
    is_website = fields.Boolean(default=False)

    def action_book(self):
        """This is used for button action  to change the state """
        self.state = 'booked'

    def action_send_event_emails(self):
        """This method is used for sending event remainder mail 2 days before the event"""
        today = fields.Date.today()
        two_days_before = today + timedelta(days=2)
        # print(two_days_before)
        events_remind = self.search([('start_date', '=', two_days_before)])
        for event in events_remind:
            template = self.env.ref('school_management.email_template_event')
            template.send_mail(event.id, force_send=True)

    def archive_events(self):
        """This method is used for archiving the past events"""
        today = date.today()
        past_events = self.search(
            [('end_date', '<', today), ('active', '=', True)])
        past_events.write({'active': False})

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        """This is used for date validation"""
        for record in self:
            if record.end_date < record.start_date:
                raise exceptions.ValidationError(
                    'Choose valid date')
