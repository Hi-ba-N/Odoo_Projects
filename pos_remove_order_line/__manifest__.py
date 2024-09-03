{
    'name': "Remove Order Line",
    'version': '17.0.1.0.0',
    'depends': ['point_of_sale'],
    'author': "Hiba",
    'category': 'Category',
    'description': "Remove Order Line",
    'data': [
      # 'views/product_template_views.xml',

    ],
'assets': {
        'point_of_sale._assets_pos': [
            'pos_remove_order_line/static/src/clear_button.xml',
            'pos_remove_order_line/static/src/remove_order_line.js',
            'pos_remove_order_line/static/src/orderline.xml',
            'pos_remove_order_line/static/src/orderline.js'
            # 'pos_rating/static/src/product_card.xml',
            # 'pos_rating/static/src/orderline.js',
            # 'pos_rating/static/src/orderline.xml'
        ],
    },


}