from itertools import product

from odoo import http
from odoo.http import request


class CartUpdate(http.Controller):

    @http.route(['/shop/<model("product.template"):product>'], type='http', auth="public",
                methods=['POST'], website=True)
    def cart_update(self):
        bom_product = request.env['res.config.settings'].sudo().search('product_id')
        product_context = dict(request.env.context, active_id=bom_product)
        bom_id = request.env['mrp.production'].sudo().search('bom_id')
        if bom_product in product_context:
            print('ff')











