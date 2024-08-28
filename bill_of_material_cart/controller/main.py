from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class ProductBomController(WebsiteSale):

    # @http.route('/get_product_bom', type='json', auth='public', website=True)
    # def get_product_bom(self, product_id):
    #     bom_data = []
    #     product = request.env['product.template'].browse(product_id)
    #
    #     for bom in product.bom_ids:
    #         bom_data.append({
    #             'name': bom.product_tmpl_id.name,
    #             'quantity': bom.product_qty,
    #         })
    #         print(bom_data)
    #
    #     return {'bom_data': bom_data}

    @http.route()
    def cart(self, access_token=None, revive='', **post):
        result = super().cart(access_token, revive, **post)
        for order in result.qcontext['website_sale_order'].order_line:
            product = order.product_id
            # print(product)
            bom_data = []
            # bom_data = request.env['mrp.production'].search('bom_id', '=', product)
            # print(bom_data)
            # print('bom', bom_data)
            for bom in product.bom_ids:
                bom_data.append({
                    'name': bom.product_tmpl_id.name,
                                'quantity': bom.product_qty,

                })

            result.qcontext.update({'bom': bom_data})
            print(result.qcontext)
        return result
