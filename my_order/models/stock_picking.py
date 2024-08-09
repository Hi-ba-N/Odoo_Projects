from odoo import fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    sales_person = fields.Many2one('res.users','sales Person')

    def button_validate(self):
        self.sales_person = self.sale_id.user_id.id
        print(self.sales_person)

#