# coding: utf-8
from odoo import fields, models


class SaleOrder(models.Model):
    """This is used for adding new state in sale order """
    _inherit = 'sale.order'

    state = fields.Selection(
        selection_add=[('admitted', "Admitted")])
