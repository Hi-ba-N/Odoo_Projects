# coding: utf-8
from odoo import api, models
from odoo.exceptions import ValidationError


class SchoolManagementLeaveReport(models.AbstractModel):
    """This is leave report abstract model"""
    _name = 'report.school_management.report_exam'

    @api.model
    def _get_report_values(self, docids, data=None):
        """This is used  to get the report action and  return  its data"""
        print('check')
        query = " "

        params = []
        print(type(data['class_ids']))
        if data['student_ids']:
            query = """SELECT sr.first_name AS student_name,sr.id as student_id, sc.name AS exam_name, sl.name as class_name, sl.id as class_id
                    FROM student_registration sr
                    JOIN student_exams_student_registration_rel sp ON sr.id = student_registration_id
                    JOIN student_exams sc ON sc.id = student_exams_id
                    join student_class sl on sr.id= sl.id 
                    where sr.id IN %s"""
            params.append(tuple(data['student_ids']))
            print(query)
            print(tuple(params))
        elif data['class_ids']:
            print('')
            query = """SELECT  sc.name AS class_name, sc.id as class_id,sl.name as exam_name
                    FROM student_class sc
                    JOIN student_exams_student_registration_rel sp ON sc.id = student_exams_id
                    join student_exams sl on sc.id = sl.id where sc.id IN %s
                    """
        params.append(tuple(data['class_ids']))

        print('query', query)
        print('params', params)

        self.env.cr.execute(query , tuple(params))
        print('haii')
        report = self.env.cr.dictfetchall()
        if not report:
            print('no result')
            raise ValidationError("No related report found")

        return {
            'doc_ids': docids,
            'doc_model': 'leave.report.wizard',
            'data': data,
            'report': report
        }
