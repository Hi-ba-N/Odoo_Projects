
from odoo import _ , models
from odoo.exceptions import ValidationError


# from odoo.addons.payment import utils as payment_utils


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
            'surl': 'https://test-payment-middleware.payu.in/simulatorResponse',
            'furl': 'https://test-payment-middleware.payu.in/simulatorResponse',
            'api_url': api_url,


        }
        payu_values['hash'] = self.provider_id._payu_generate_sign(
            payu_values, incoming=False,
        )
        print(payu_values)
        # print(payu_values['hash'])
        return payu_values

    def _get_tx_from_notification_data(self, provider_code,
                                       notification_data):
        """ Override of payment to find the transaction based on Payu data."""
        print('gettxn work')
        tx = super()._get_tx_from_notification_data(provider_code,
                                                    notification_data)
        print(notification_data)
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
        print('tx',tx)

        return tx

    def _process_notification_data(self, notification_data):
        print('process data working')
        """ Override of payment to process the transaction based on Payu data.

        Note: self.ensure_one()

        :param dict notification_data: The notification data sent by the provider
        :return: None
        """
        super()._process_notification_data(notification_data)
        if self.provider_code != 'payu':
            return

        # Update the provider reference.
        self.provider_reference = notification_data.get('payuId')

        # Update the payment method
        payment_method_type = notification_data.get('bankcode', '')
        payment_method = self.env['payment.method']._get_from_code(payment_method_type)
        self.payment_method_id = payment_method or self.payment_method_id
        print(payment_method_type)
        # Update the payment state.
        status = notification_data.get('status')
        if status == 'success':
            self._set_done()
        else:
            error_code = notification_data.get('Error')
            self._set_error(
                "PayU: " + _("The payment encountered an error with code %s", error_code)
            )

