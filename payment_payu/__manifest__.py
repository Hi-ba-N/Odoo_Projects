{
    'name': 'Payment Provider: PayU',
    'version': '17.0.1.0.0',
    'category': 'Accounting/Payment Providers',
    'description': "Payment Provider PayU ",
    'author': 'Hiba ',
    'depends': ['payment'],
    'data': [

     'views/payment_provider_views.xml',
      'views/payment_payu_template.xml',
        'data/payment_provider_data.xml'
    ],

    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook',
    'license': 'LGPL-3'
}