# coding: utf-8
from odoo import fields, models


class ProductTemplate(models.Model):
    """ This is used for inheriting product and calculating average cost"""
    _inherit = 'product.template'

    avg_cost = fields.Float(compute="_compute_average_cost",
                            string="Average Cost")

    def _compute_average_cost(self):
        for record in self:
            purchase_order = self.env['purchase.order.line'].search(
                ['&', ('state', 'in', ['purchase', 'done']),
                 ('product_id', 'in', record.product_variant_ids.ids)])
            total_cost = sum(
                rec.price_unit * rec.product_qty for rec in purchase_order)
            total_quantity = sum(rec.product_qty for rec in purchase_order)
            print("cost", total_cost)
            print("qty", total_quantity)
            if total_quantity:
                avg = total_cost / total_quantity
                self.avg_cost = avg
            else:
                self.avg_cost = 0.0



