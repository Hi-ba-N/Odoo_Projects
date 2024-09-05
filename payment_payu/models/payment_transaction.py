from odoo import models


class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    def _get_specific_rendering_values(self, processing_values):
        print(processing_values)
        res = super()._get_specific_rendering_values(processing_values)
        if self.provider_code != 'payu':
            return res
        payu_values = {
            'key': self.provider_id.payumoney_merchant_key,
            'txnid': '',
            'firstname': self.partner_name,
            'amount': self.amount,
            'email': self.partner_email,
            'phone': self.partner_phone,
        }






































        # res = super()._get_specific_rendering_values(processing_values)
        # if self.provider_code != 'payu':
        #     return res
        # first_name = self.partner_id.name
        # payu_values = {
        #     'key': self.provider_id.payu_merchant_key,
        #     'txnid': self.reference,
        #     'amount': self.amount,
        #     'productinfo': self.reference,
        #     'firstname': first_name,
        #     'email': self.partner_email,
        #     'phone': self.partner_phone
        #
        # }
