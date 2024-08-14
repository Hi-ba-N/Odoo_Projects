from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_only_order = fields.Boolean('Is only ordered')
