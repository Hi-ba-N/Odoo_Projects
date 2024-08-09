# coding: utf-8
from odoo import api, fields, models, exceptions
from odoo.tools import date_utils


class StudentLeaves(models.Model):
    """this  is used for Student leave"""
    _name = 'student.leave'
    _description = "Student Leave"
    _inherit = 'mail.thread'
    _rec_name = 'student_id'

    student_id = fields.Many2one(
        'student.registration',
        domain="[ ('state', '=', 'registration')]",
        string='Student'
    )
    class_id = fields.Many2one(
        string='Class',
        related='student_id.student_class_id')
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    total_days = fields.Integer(compute="_compute_total_days",
                                store=True)
    half_day = fields.Boolean("Half Day")
    reason = fields.Char("Reason")

    @api.depends("start_date", "end_date")
    def _compute_total_days(self):
        """This is used for computing total days based on start date and end date except saturday and sunday"""
        for record in self:
            if record.start_date and record.end_date:
                total_days = 0
                current_date = record.start_date
                while current_date <= record.end_date:
                    if current_date.weekday() < 5:
                        total_days += 1
                    current_date += date_utils.relativedelta(days=1)
                    # print(current_date)
                record.total_days = total_days

            else:
                record.total_days = 0

    @api.constrains('start_date', 'end_date', 'half_day')
    def _check_half_day(self):
        """This is used for half day validation"""
        for record in self:
            if record.half_day:
                if record.start_date != record.end_date:
                    raise exceptions.ValidationError(
                        'start date and end date must be the same for half day.')

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        """This is used for date validation"""
        for record in self:
            if record.end_date < record.start_date:
                raise exceptions.ValidationError(
                    'Choose valid date')



