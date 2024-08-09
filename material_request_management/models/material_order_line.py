# coding: utf-8
from odoo import api, fields, models


class MaterialOrderLine(models.Model):
    """This model is used for viewing product quantity and price through wizard."""
    _name = 'material.order.line'
    _description = "Material Order line"

    request_id = fields.Many2one('material.request',
                                 string='Material Request', required=True,
                                 ondelete='cascade')
    product_id = fields.Many2one('product.product', string='Product',
                                 required=True)
    material_action = fields.Selection(
        [('purchase', 'Purchase Order'), ('transfer', 'Internal Transfer')],
        string=' Request Action', required=True)
    quantity = fields.Float(string='Quantity', required=True, default=1.0)
    source_location_id = fields.Many2one('stock.location',
                                         string='Source Location',
                                         )
    destination_location_id = fields.Many2one('stock.location',
                                              string='Destination Location',
                                              )



