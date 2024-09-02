{
    'name': "POS Purchase Limit",
    'version': '17.0.1.0.0',
    'depends': ['point_of_sale'],
    'author': "Hiba",
    'category': 'Category',
    'description': "POS Purchase Limit",
    'data': [
      'views/res_partner_views.xml',

    ],
'assets': {
        'point_of_sale._assets_pos': [
            'pos_purchase_limit/static/src/payment_screen.js',
            'pos_purchase_limit/static/src/payment_order.js'

        ],
    },


}