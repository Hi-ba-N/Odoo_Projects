# coding: utf-8
from odoo import fields, models


class ProductWizard(models.TransientModel):
    """This model is used for viewing product quantity and price through wizard."""
    _name = 'product.wizard'
    _description = "Product Wizard"
    quantity = fields.Float(string="Quantity")
    price = fields.Float(string="Price")
