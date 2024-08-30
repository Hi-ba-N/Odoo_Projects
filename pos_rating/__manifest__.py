{
    'name': "POS Rating",
    'version': '17.0.1.0.0',
    'depends': ['point_of_sale','product','base'],
    'author': "Hiba",
    'category': 'Category',
    'description': "POS Rating",
    'data': [
      'views/product_template_views.xml',

    ],
'assets': {
        'point_of_sale._assets_pos': [
            'pos_rating/static/src/product_rating.js',
            'pos_rating/static/src/product_card.xml',
            'pos_rating/static/src/orderline.js',
            'pos_rating/static/src/orderline.xml'
        ],
    },


}