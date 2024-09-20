from odoo import models


class LoyaltyProgram(models.Model):
    _inherit = 'loyalty.program'

    def apply_loyalty(self, order):
        for reward in self.reward_ids:
            # Example logic for applying a discount reward directly to the order
            if reward.reward_type == 'discount':
                discount = reward.discount / 100 * order.amount_total
                print(discount)
                order.amount_total -= discount
                print(order.amount_total)
                # order.message_post(body='5% E-Commerce Discount applied automatically.')