from odoo import models


class LoyaltyProgram(models.Model):
    _inherit = 'loyalty.program'

    def apply_loyalty(self, order):
        for reward in self.reward_ids:
            if reward.reward_type == 'discount':
                print(order.amount_total)
                discount = order.amount_total * reward.discount / 100
                print(discount)
                order.amount_total -= discount
                print(order.amount_total)
