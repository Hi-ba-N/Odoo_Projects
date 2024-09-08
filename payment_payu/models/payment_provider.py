# coding: utf-8
import hashlib

from odoo import fields, models


class PaymentProvider(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(
        selection_add=[('payu', 'Payu')], ondelete={'payu': 'set default'}
    )
    payu_merchant_key = fields.Char(
        string="Merchant Key",
        required_if_provider="payu"
    )
    # payu_merchant_salt = fields.Char(
    #     string="Merchant Salt", required_if_provider='payu'
    #     )

    def _get_supported_currencies(self):
        """ Override of `payment` to return INR as the only supported currency. """
        supported_currencies = super()._get_supported_currencies()
        print(supported_currencies)
        if self.code == 'payu':
            supported_currencies = supported_currencies.filtered(
                lambda c: c.name == 'INR')
        print('kk', supported_currencies)
        return supported_currencies


    def _payu_generate_sign(self, values, incoming=True):
        """ Generate the hash for incoming or outgoing communications."""
        sign_values = {
            **values,
            'key': self.payu_merchant_key,
            'salt': '4R38IvwiV57FwVpsgOvTXBdLE4tHUXFW'
        }
        print(sign_values['salt'])
        if incoming:

            keys = 'salt|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|' \
                   'txnid|key'
            sign = '|'.join(f'{sign_values.get(k) or ""}' for k in keys.split('|'))
        else:
            print('else')
            keys = 'key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt'
            sign = '|'.join(f'{sign_values.get(k) or ""}' for k in keys.split('|'))
        return hashlib.sha512(sign.encode('utf-8')).hexdigest()



