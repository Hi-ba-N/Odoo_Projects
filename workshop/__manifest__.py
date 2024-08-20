# -*- coding: utf-8 -*-
{
    'name': 'WorkShop',
    'version': '1.0.0',
    'depends': ['web','sale_management',],
    'website': "https://www.cyllo.com",
    'data': [
        'views/workshop_view.xml',
    ],
    'assets': {
        # 'web.assets_backend': [
        #     'workshop/static/src/js/**/*'
        # ],
    },
    'license': "LGPL-3",
    'installable': True,
    'auto_install': False,
    'application': True,
}
