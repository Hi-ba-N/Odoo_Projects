{
    'name': "School Management",
    'version': '17.0.6.0.0',
    'depends': ['base',
                'mail', 'sale','website'],
    'author': "Hiba",
    'category': 'Category',
    'description': "School Management",
    'application': True,
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'security/ir_rule.xml',
        'data/ir_sequence_data.xml',
        'data/ir_actions_server_data.xml',
        'data/student_department_data.xml',
        'data/student_subject_data.xml',
        'data/student_class_data.xml',
        'data/student_academic_data.xml',
        'data/email_template_data.xml',
        'data/ir_cron_data.xml',
        'views/student_registration_views.xml',
        'views/student_list_views.xml',
        'views/student_department_views.xml',
        'views/student_class_views.xml',
        'views/student_academic_views.xml',
        'views/student_subject_views.xml',
        'views/student_clubs_views.xml',
        'views/student_event_views.xml',
        'views/res_partner_views.xml',
        'views/student_leave_views.xml',
        'views/student_exams_views.xml',
        'views/student_papers_views.xml',
        'views/student_teachers_views.xml',
        'views/student_staff_views.xml',
        'views/sale_order_views.xml',
        'wizard/leave_report_wizard_views.xml',
        'wizard/event_report_wizard_views.xml',
        'wizard/club_report_wizard_views.xml',
        'wizard/class_report_wizard_views.xml',
        'wizard/exam_report_wizard_views.xml',
        'report/leave_report.xml',
        'report/event_report.xml',
        'report/club_report.xml',
        'report/class_report.xml',
        'report/exam_report.xml',
        'views/student_menus.xml',
        'report/ir_actions_report.xml',
        'views/register_form_template.xml',
        'views/register_form_success_template.xml',
        'views/register_tree_template.xml',
        'views/leave_form_template.xml',
        'views/leave_form_success_template.xml',
        'views/leave_tree_template.xml',
        'views/event_form_template.xml',
        'views/event_form_success_template.xml',
        'views/event_tree_template.xml',
         'views/website_snippet.xml',
         'views/website_menus.xml'

    ],
'assets': {
        'web.assets_frontend': [
            'school_management/static/src/js/date_validation.js',
            'school_management/static/src/js/leave_days_calculator.js',
            'school_management/static/src/xml/dynamic_courosel.xml',
            'school_management/static/src/js/snippet.js'

        ],
    },
'assets': {
        'web.assets_backend': [
            'school_management/static/src/js/action_manager.js'


        ],
    }

}