{
    'name': "Hospital",
    'application': 'True',
    'depends': [
                'hr',
                'hr_hourly_cost'
                ],
    'data': [

        'views/hospital_doctor_views.xml',
        # 'views/hospital_op.xml',
         # 'views/hospital_views.xml',
        'views/hospital_menus.xml',
         'views/hospita_op_sequence.xml',
        'security/ir.model.access.csv',
    ]

}
