# coding: utf-8
from odoo import fields, models


class SaleOrder(models.Model):
    """This is used for adding new state in sale order """
    _inherit = 'sale.order'

    def check_partner(self):
        invoice_product = self.env['product.template'].search(
            [('invoice_policy', '=', 'order')])
        contacts =self.env['res.partner'].search([('is_only_order','=',True)])

        if self.id.partner_id == contacts:
            






