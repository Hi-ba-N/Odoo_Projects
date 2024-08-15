# coding: utf-8
<<<<<<< HEAD
from odoo import fields, models, exceptions


class SaleOrder(models.Model):
    """"""
=======
from odoo import fields, models


class SaleOrder(models.Model):
    """This is used for adding new state in sale order """
>>>>>>> d6f0197172a30655fb4f75c274aba406265d547e
    _inherit = 'sale.order'

    def check_partner(self):
        invoice_product = self.env['product.template'].search(
            [('invoice_policy', '=', 'order')])
<<<<<<< HEAD
        contacts = self.env['res.partner'].search([('is_only_order', '=', True)])

        if self.partner_id in contacts:
            for line in self.order_line:
                if line.product_id not in invoice_product:
                    raise exceptions.ValidationError(
                        "This partner can only order products with the "
                    )
=======
        contacts =self.env['res.partner'].search([('is_only_order','=',True)])

        if self.id.partner_id == contacts:
            






>>>>>>> d6f0197172a30655fb4f75c274aba406265d547e
