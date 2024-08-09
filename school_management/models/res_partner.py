 # coding: utf-8
from odoo import api, fields, models, Command
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    """This is used for Employees """
    _inherit = 'res.partner'

    role = fields.Selection(
        string='Role',
        selection=[("teacher", "Teacher"),
                   ("office_staff", "Office Staff")])

    @api.constrains('email')
    def _check_email(self):
        """This function is used for email validation"""
        count_email = self.search_count([('email', '=', self.email)])
        if count_email > 1 and self.email is not False:
            raise ValidationError(
                'The email already registered, please use another email!')

    def create_user_teacher(self):
        """This is used for creating teacher user"""
        if self.role == 'office_staff':
            user_vals = {
                'name': self.email,
                'login': self.email,
                'groups_id': [
                    Command.link(
                        self.env.ref('school_management.group_staff').id)]

            }
            new_user = self.env['res.users'].create(user_vals)

    def create_user_staff(self):
        """This is used for creating staff group"""
        if self.role == 'teacher':
            user_vals = {
                'name': self.email,
                'login': self.email,
                'groups_id': [
                    Command.link(
                        self.env.ref('school_management.group_teacher').id)]

            }
            new_user = self.env['res.users'].create(user_vals)
