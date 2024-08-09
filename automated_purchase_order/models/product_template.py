# coding: utf-8
from odoo import models


class ProductTemplate(models.Model):
    """ This is used for inheriting product and calculating average cost"""
    _inherit = 'product.template'

    def action_wizard(self):
        """This is used for wizard button action"""
        product_cost = self.env['product.wizard'].create({
            'product_id': self.id,
            'price': self.standard_price,

        })

        return {
            'type': 'ir.actions.act_window',
            'name': 'Product',
            'res_model': 'product.wizard',
            'target': 'new',
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': product_cost.id,
        }






















