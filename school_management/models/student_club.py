# coding: utf-8
from odoo import fields, models


class StudentClub(models.Model):
    """This is used for student club"""
    _name = "student.club"
    _description = "Club"
    _inherit = 'mail.thread'

    name = fields.Char(string="Name", required=True)
    description = fields.Html(String='Description')
    student_ids = fields.Many2many('student.registration', string='Student', domain="[ ('state', '=', 'registration')]")
    event_count = fields.Integer(compute='_compute_count')

    def get_events(self):
        """This is used for getting event detail"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Events',
            'view_mode': 'tree',
            'res_model': 'student.event',
            'domain': [('club_id', '=', self.id)],
            'context': "{'create': False}"
        }

    def _compute_count(self):
        """This is used for counting events """
        for record in self:
            record.event_count = self.env['student.event'].search_count(
                [('club_id', '=', self.id)])


