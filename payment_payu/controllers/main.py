# coding: utf-8
from odoo import http
from odoo.http import request


class PayUController(http.Controller):
    _return_url = '/payment/payu/return'
    @http.route(
        _return_url, type='http', auth='public', methods=['GET', 'POST'],
        csrf=False,
        save_session=False
    )
    def payu_return_from_checkout(self, **data):
        """ Process the notification data sent by PayU after redirection from checkout."""
        print('redirect')
        print(data)
        request.env['payment.transaction'].sudo()._handle_notification_data(
            'payu', data)
        return request.redirect('/payment/status')
