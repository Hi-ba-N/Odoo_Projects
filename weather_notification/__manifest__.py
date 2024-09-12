# -*- coding: utf-8 -*-
{
    'name': 'Weather Notification',
    'version': '17.0.1.0.0',
    'depends': ['web','hr'],
    'author': "Hiba",
    'description': "Weather Notification",
    'data': [
        'views/res_users_view.xml',
        'views/res_users_profile_view.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'weather_notification/static/src/js/weather.js',
            'weather_notification/static/src/xml/weather_icon.xml'
        ],
    },
    'license': "LGPL-3",
    'installable': True,
    'application': True,
}