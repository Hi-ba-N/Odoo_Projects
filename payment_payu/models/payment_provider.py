# coding: utf-8
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

    def _get_supported_currencies(self):
        """ Override of `payment` to return INR as the only supported currency. """
        supported_currencies = super()._get_supported_currencies()
        print(supported_currencies)
        if self.code == 'payu':
            supported_currencies = supported_currencies.filtered(
                lambda c: c.name == 'INR')
        print('kk', supported_currencies)
        return supported_currencies


