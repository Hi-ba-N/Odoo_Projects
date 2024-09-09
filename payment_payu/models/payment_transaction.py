# coding: utf-8
# from importlib.resources import _

from werkzeug import urls

from odoo.addons.payment_payu.controllers.main import PayUController

from odoo import _, models
from odoo.exceptions import ValidationError


class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    def _get_specific_rendering_values(self, processing_values):
        res = super()._get_specific_rendering_values(processing_values)
        print(processing_values)
        api_url = 'https://test.payu.in/_payment'
        if self.provider_code != 'payu':
            return res
        payu_values = {
            'key': self.provider_id.payu_merchant_key,
            'txnid': self.reference,
            'productinfo': self.reference,
            'firstname': self.partner_id.name,
            'amount': self.amount,
            'email': self.partner_email,
            'phone': self.partner_phone,
            'return_url': urls.url_join(self.get_base_url(),
                                        PayUController._return_url),

            'api_url': api_url,

        }
        payu_values['hash'] = self.provider_id._payu_generate_sign(
            payu_values
        )
        print(payu_values['hash'])
        return payu_values

    def _get_tx_from_notification_data(self, provider_code,
                                       notification_data):
        """ Override of payment to find the transaction based on Payu data."""
        print('gettxn work')
        tx = super()._get_tx_from_notification_data(provider_code,
                                                    notification_data)
        print('tx', tx)
        if provider_code != 'payu' or len(tx) == 1:
            return tx

        reference = notification_data.get('txnid')
        if not reference:
            raise ValidationError(
                "PayU: " + _(
                    "Received data with missing reference (%s)", reference)
            )

        tx = self.search([('reference', '=', reference),
                          ('provider_code', '=', 'payu')])

        if not tx:
            raise ValidationError(
                "PayU: " + _(
                    "No transaction found matching reference %s.",
                    reference)
            )
        print('tx2', tx)

        return tx

    def _process_notification_data(self, notification_data):
        """ Override of payment to process the transaction based on Payu data. """
        print('process data working')
        super()._process_notification_data(notification_data)
        self.provider_reference = notification_data.get('mihpayid')


        status = notification_data.get('status')
        if status == 'success':
            self._set_done()
            # sale_order = self.sale_order_ids
            # print(sale_order)

            # if self.sale_order_ids:
            #     print('sale order')
            #
            #     self.sale_order_ids.action_confirm()
            #     self.sale_order_ids._create_invoices()
            #     for invoice in self.sale_order_ids.invoice_ids:
            #         invoice.action_post()

                # invoice.action_post()
        else:
            error_code = notification_data.get('error')
            print(error_code)
            self._set_error(
                "PayU: " + _(notification_data.get('error_Message'))

            )
