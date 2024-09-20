from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleDiscount(WebsiteSale):

    @http.route()
    def cart(self, access_token=None, revive='', **post):
        result = super().cart(access_token, revive, **post)
        order = request.website.sale_get_order()
        if order and order.website_id:
            print('website')
            promotion_program = request.env['loyalty.program'].sudo().search([
                ('name', '=', '5% Discountt'),
                ('active', '=', True)
            ], limit=1)
            if promotion_program:
                discount_percentage = 5.0
                total_discount = (order.amount_total * discount_percentage) / 100
                print(total_discount)

                # Apply the discount directly to the total amount
                order.write({
                    'amount_total': order.amount_total - total_discount
                })

                # Display message in green for successful application of the promotion
                result.qcontext['promotion_message'] = "Promotion applied"
                result.qcontext['promotion_message_class'] = "text-success"  # Bootstrap class for green text

                # Return the updated cart view with the message
            print(result.qcontext)
            return result

        #         print(order.amount_total)
        #         discount_value = promotion_program.reward_ids.discount
        #         print(discount_value)
        #         discount_total = order.amount_total * discount_value / 100
        #         total_discount = order.amount_total - discount_total
        #         print(discount_total)
        #         print(total_discount)
        #         # order.amount_total -= order.amount_total * discount_value / 100
        #         print(order.amount_total)
        #         # promotion_program.apply_loyalty(order)
        #         result.qcontext.update({'discount_total': total_discount})
        #         print(result.qcontext)
        # return result
        #
