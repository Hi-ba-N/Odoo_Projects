from odoo import models


class PosSession(models.Model):
    _inherit = 'pos.session'

    def _loader_params_product_product(self):
        result = super()._loader_params_product_product()
        # print(result)
        result['search_params']['fields'].append('product_rating')
        print(result)
        return result


