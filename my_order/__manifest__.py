{
    'name': "My Order",
    'version': '17.0.1.0.0',
    'depends': ['sale','stock'],
    'author': "Hiba",
    'category': 'Category',
    'description': "My Order",
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/my_order_views.xml',
        'views/my_order_menus.xml',
    ]

}