
from odoo import http
from odoo.http import request


class ProductBomController(http.Controller):

    @http.route('/get_product_bom', type='json', auth='public', website=True)
    def get_product_bom(self, product_id):
        bom_data = []
        product = request.env['product.template'].browse(product_id)

        for bom in product.bom_ids:
            bom_data.append({
                'name': bom.product_tmpl_id.name,
                'quantity': bom.product_qty,
            })
            print(bom_data)

        return {'bom_data': bom_data}

