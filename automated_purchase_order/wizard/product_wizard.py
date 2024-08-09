# coding: utf-8
from odoo import fields, models, Command
from odoo.exceptions import ValidationError


class ProductWizard(models.TransientModel):
    """This model is used for viewing product quantity and price through wizard."""
    _name = 'product.wizard'
    _description = "Product Wizard"

    quantity = fields.Float(string="Quantity", default=1)
    price = fields.Float(string="Price", required=True, readonly=True)
    product_id = fields.Many2one('product.template', 'Product')

    def action_confirm(self):
        """ This is used for selecting top vendor , if there is any existing rfq
        for the vendor update it else create new rfq"""
        vendor = self.product_id
        if self.product_id.seller_ids:
            vendor = self.product_id.seller_ids[0].partner_id
            print(vendor.name)
        else:
            raise ValidationError(
                "No vendor is available")
        existing_rfq = self.env['purchase.order'].search([
            ('partner_id', '=', vendor.id),
            ('state', '=', 'draft')
        ], limit=1)
        if existing_rfq:
            self.env['purchase.order.line'].create({
                'order_id': existing_rfq.id,
                'product_id': self.product_id.product_variant_ids.id,
                'product_qty': self.quantity,
                'price_unit': self.price,
            })

            print('existing rfq')

        else:
            order_line = self.env['purchase.order'].create({
                'partner_id': vendor.id,
                'order_line': [Command.create({
                    'product_id': self.product_id.product_variant_ids.id,
                    'product_qty': self.quantity,
                    'price_unit': self.price
                }
                )],
            })
            print('new rfq')
            order_line.button_confirm()













