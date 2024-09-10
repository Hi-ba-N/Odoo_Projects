# -*- coding: utf-8 -*-
{
    'name': 'Weather Notification',
    'version': '17.0.1.0.0',
    'depends': ['web'],
    'author': "Hiba",
    'description': "Weather Notification",
    'data': [
        'views/res_users_view.xml'
    ],
    'assets': {
        'web.assets_backend': [
            # 'workshop/static/src/js/**/*'
            'weather_notification/static/src/js/weather.js',
            'weather_notification/static/src/xml/weather_icon.xml'
        ],
    },
    'license': "LGPL-3",
    'installable': True,
    'application': True,
}