# coding: utf-8
from email.policy import default

import requests

from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    is_weather_api = fields.Boolean("Activate Weather ")
    api_key = fields.Char('Weather Api Key')
    city = fields.Char('City')




