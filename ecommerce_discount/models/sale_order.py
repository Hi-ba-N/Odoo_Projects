from odoo import models, api, fields
from odoo.exceptions import UserError
from odoo.http import request

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _auto_apply_rewards(self):
        """
        Tries to auto apply claimable rewards.

        The reward must follow these rules:
        - Must not be from a nominative program
        - The reward must be the only reward of the program
        - The reward may not be a multi-product reward
        """
        for order in self:
            claimable_rewards = order._get_claimable_rewards()
            print(claimable_rewards)
            for coupon, rewards in claimable_rewards.items():
                if (
                    len(coupon.program_id.reward_ids) != 1  # Only one reward per program
                    or coupon.program_id.is_nominative  # Not a nominative program
                    or (rewards.reward_type == 'product' and rewards.multi_product)  # Not multi-product
                ):
                    continue

                # Try to apply the reward
                try:
                    result = order._apply_program_reward(rewards, coupon)
                    print(result)
                    if 'error' in result:
                        raise UserError(result['error'])
                except UserError as e:
                    continue  # Ignore errors during reward application

    @api.model
    def create(self, vals):
        # Override the create method to auto-apply promotions on order creation
        order = super(SaleOrder, self).create(vals)
        order._update_programs_and_rewards()
        # Update programs
        order._auto_apply_rewards()
        # Automatically apply rewards
        print(order)
        return order

    def write(self, vals):
        # Override the write method to auto-apply promotions on order update
        result = super(SaleOrder, self).write(vals)
        self._update_programs_and_rewards()  # Update programs
        self._auto_apply_rewards()  # Automatically apply rewards
        print(result)
        return result

    def _get_claimable_rewards(self):
        """
        This method retrieves rewards that are eligible to be claimed.
        """
        self.ensure_one()
        claimable_rewards = super(SaleOrder, self)._get_claimable_rewards()
        print(claimable_rewards)
        return claimable_rewards

    def _apply_program_reward(self, reward, coupon):
        """
        Apply the given reward to the order.
        """
        self.ensure_one()
        # You can add logic here to apply the reward based on your specific requirements
        return super(SaleOrder, self)._apply_program_reward(reward, coupon)

