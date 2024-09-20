from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleDiscount(WebsiteSale):

    @http.route()
    def cart(self, access_token=None, revive='', **post):
        print('hello')
        result = super().cart(access_token, revive, **post)
        order = request.website.sale_get_order()

        # Apply promotion only for E-Commerce orders
        if order and order.website_id:
            # Look for a specific promotion (e.g., "5% E-Commerce Discount")
            promotion_program = request.env['loyalty.program'].sudo().search([
                ('name', '=', '5 % Discountt'),
                ('active', '=', True)
            ], limit=1)

            # Apply the promotion automatically if found
            if promotion_program and not order.applied_coupon_ids:
                # Apply promotion by adding the corresponding reward
                promotion_program.apply_loyalty(order)

        return result