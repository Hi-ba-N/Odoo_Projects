{
    'name': "Material Request Management",
    'version': '17.0.1.0.0',
    'depends': ['base','hr','mail','stock'],
    'author': "Hiba",
    'category': 'Material Request/Material Request Management',
    'description': "Material Request",
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/material_request_views.xml',
        'views/material_order_line_views.xml',
        'views/material_request_menu.xml',
    ],
    'license': 'LGPL-3',

}