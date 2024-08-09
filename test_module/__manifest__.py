{
    'name': "Test Module",
    'version': '17.0.1.0.0',
    'depends': ['web'],
    'author': "Hiba",
    'description': "Test Module",
    'data': [
    'views/ir_actions_client.xml'
    ],

    'assets': {
        'web.assets_backend': [
            'test_module/static/src/js/test.js',
            'test_module/static/src/xml/test_template.xml',
            'test_module/static/src/js/demo_component.js',
            'test_module/static/src/xml/demo_component_template.xml'
        ],
    },

    'license': 'LGPL-3',

}