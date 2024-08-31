# coding: utf-8
from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    activate_purchase_limit = fields.Boolean('Activate Purchase Limit')
    purchase_limit = fields.Float('Purchase Limit')
