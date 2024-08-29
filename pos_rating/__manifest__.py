{
    'name': "POS Rating",
    'version': '17.0.1.0.0',
    'depends': ['base','purchase'],
    'author': "Hiba",
    'category': 'Category',
    'description': "POS Rating",
    'data': [
      'views/product_template_views.xml',

    ],
'assets': {
        'point_of_sale._assets_pos': [
            'pos_rating/static/src/js/product_rating.js',
            'pos_rating/static/src/overrides/components/product_rating/product_cad.xml'
        ],
    },


}