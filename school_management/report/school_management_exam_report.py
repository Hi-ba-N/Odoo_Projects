# coding: utf-8
from odoo import api, models
from odoo.exceptions import ValidationError


class SchoolManagementExamReport(models.AbstractModel):
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
            query = """  SELECT se.name as exam_name, sc.name as class_name, sr.id as student_id, sr.first_name as student_name,se.id as exam_id
                      FROM student_exams se
                      JOIN student_class sc ON se.class_id = sc.id

                      JOIN student_registration sr ON sr.student_class_id = sc.id
                      WHERE sr.id IN %s"""
            params.append(tuple(data['student_ids']))
            print(tuple(params))
        elif data['class_ids']:
            print('')
            query = """SELECT se.name as exam_name, sc.name as class_name,sc.id as class_id
                      FROM student_exams se
                      JOIN student_class sc ON se.class_id = sc.id
                      WHERE sc.id IN %s
                                  """
            params.append(tuple(data['class_ids']))
        elif data['exam_ids']:
            query = """
                              SELECT se.name as exam_name, sc.name as class_name, ss.name as subject_name
                              FROM student_exams se
                              JOIN student_class sc ON se.class_id = sc.id
                              JOIN student_paper sp ON sp.exam_id = se.id
                              JOIN student_subject ss ON sp.subject_id = ss.id
                              WHERE se.id IN %s
                          """
            params.append(tuple(data['exam_ids']))

        self.env.cr.execute(query, params)
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
