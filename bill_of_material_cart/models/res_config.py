# -*- coding: utf-8 -*-
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    is_select_multiple_products = fields.Boolean(
        string='Select Multiple Products'
    )
    product_id = fields.Many2many('product.template', string='Products')








