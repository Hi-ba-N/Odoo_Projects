# coding: utf-8

from odoo import fields, models, exceptions, api


class SaleOrder(models.Model):


    _inherit = 'sale.order'


    # def check_partner(self):
    #     invoice_product = self.env['product.template'].search(
    #         [('invoice_policy', '=', 'order')])
    #
    #     contacts = self.env['res.partner'].search([('is_only_order', '=', True)])
    #
    #     if self.partner_id in contacts:
    #         for line in self.order_line:
    #             if line.product_id not in invoice_product:
    #                 raise exceptions.ValidationError(
    #                     "This partner can only order products with the "
    #                 )
    # @api.onchange('dob')
    # def check_customer_refernce(self):
    #     if self.client_order_ref

    _sql_constraints = [
                ('aadhaar_uniq', 'unique(client_order_ref)',
                 "Customer Reference  must be unique"),
    ]








