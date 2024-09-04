# coding: utf-8
from odoo import fields, models


class PaymentProvider(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(
        selection_add=[('payu', 'Payu')], ondelete={'payu': 'set default'}
    )
    merchant_key = fields.Char(
        string="Merchant Key",
        required_if_provider="payu"
    )


