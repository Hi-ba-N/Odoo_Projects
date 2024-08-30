# coding: utf-8
from odoo import fields, models


class ProductProduct(models.Model):
    """ This is used for inheriting product and new field as product rating"""
    _inherit = 'product.product'

    product_rating = fields.Selection(
        string='Product Rating',
        selection=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")])

