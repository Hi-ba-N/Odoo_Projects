from odoo import models, fields


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    sales_person = fields.char()



