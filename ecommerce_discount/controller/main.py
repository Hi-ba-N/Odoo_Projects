from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleDiscount(WebsiteSale):

    @http.route()
    def cart(self, access_token=None, revive='', **post):
        redirect = post.get('r', '/shop/cart')
        print('hello')
        result = super().cart(access_token, revive, **post)
        order = request.website.sale_get_order()
        promotion = request.env['loyalty.program'].sudo().search([
            ('name', '=', '5% Discountt'),
            ('active', '=', True)
        ], limit=1)
        print(promotion)
        if promotion:
            print('promo')
            # order._cart_update_pricelist(update_pricelist=True)

        return result


















        #         print('hkdo')
        #         discount_value = promotion.reward_ids.discount
        #         amount_total = result.qcontext.get('amount', 0.0)
        #         print(amount_total)
        #         discount_amount = amount_total * discount_value / 100
        #         amount_total -= discount_amount
        #         print(amount_total)
        #
        #         result.qcontext['amount'] = amount_total
        #         result.qcontext['discount_message'] = f"A {discount_value}% discount has been applied to your order."
        #         print(result.qcontext)
        #
        # return result

        # result = super().cart(access_token, revive, **post)
        # print(result.qcontext)
        # amount_total = result.qcontext['amount']
        # print(amount_total)
        # promotion = request.env['loyalty.program'].sudo().search([
        #     ('name', '=', '5% Discountt'),
        #     ('active', '=', True)
        # ], limit=1)
        # print(promotion)
        # if promotion:
        #     discount_value = promotion.reward_ids.discount
        #     amount_total -= amount_total * discount_value / 100
        #     print(amount_total)
        # result.qcontext['amount'] = amount_total
        # print(result.qcontext)
        # return result
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #

    # def apply_promotion_discount(self,  promotion):
    #     discount_value = promotion.reward_ids.discount
    #     print('disc', discount_value)
    #     line.price_total -= (line.price_total * discount_value / 100)
    #     print(line.price_total)

    #     confirm_order = super().confirm_order(**post)
    #     res = confirm_order.qcontext
    #     print(confirm_order)
    #     print(res)
    #     print('hello')
    #     order = request.website.sale_get_order()
    #     print(order)
    #
    #     if order:
    #         promotion = request.env['loyalty.program'].sudo().search([
    #             ('name', '=', '5% Discountt'),
    #             ('active', '=', True)
    #         ], limit=1)
    #         print(promotion)
    #         if promotion:
    #             self.apply_promotion_discount(order, promotion)
    #
    #     return
    #
    # def apply_promotion_discount(self, order, promotion):
    #     discount_value = promotion.reward_ids.discount
    #     print('disc', discount_value)
    #     for line in order.order_line:
    #         print(order.order_line)
    #         line.price_total -= (line.price_total * discount_value / 100)
    #         print(line.price_total)
