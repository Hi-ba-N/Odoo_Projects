# coding: utf-8

from odoo import fields, models, exceptions


class SaleOrder(models.Model):


    _inherit = 'sale.order'

    def check_partner(self):
        invoice_product = self.env['product.template'].search(
            [('invoice_policy', '=', 'order')])

        contacts = self.env['res.partner'].search([('is_only_order', '=', True)])

        if self.partner_id in contacts:
            for line in self.order_line:
                if line.product_id not in invoice_product:
                    raise exceptions.ValidationError(
                        "This partner can only order products with the "
                    )







