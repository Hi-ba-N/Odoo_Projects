# coding: utf-8
from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    api_key = fields.Char('Weather Api Key')
    city = fields.Char('City')
