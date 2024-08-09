{
    'name': "Automated Purchase Order",
    'version': '17.0.1.0.0',
    'depends': ['base','purchase'],
    'author': "Hiba",
    'category': 'Category',
    'description': "Automated Purchase Order",
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'wizard/product_wizard_views.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': True,
    'application': True
}