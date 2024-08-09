# coding: utf-8
from odoo import models, api


class SchoolManagementLeaveReport(models.AbstractModel):
    _name = 'report.school_management.report_exam'

    @api.model
    def _get_report_values(self, docids, data=None):
        print('check')
        query = """SELECT sl.name, sr.first_name AS student_name, sc.name AS class_name
                                  FROM student_exams sl
                                  JOIN student_registration sr ON sr.id = sl.id
                                  JOIN student_class sc ON sc.id = sr.id
                                  """

        params = []

        if data['student_ids']:
            query += " AND sl.id IN %s"
            params.append(tuple(data['student_ids']))

        self.env.cr.execute(query, params)
        report = self.env.cr.dictfetchall()
        print(report)

        return {
            'doc_ids': docids,
            'doc_model': 'leave.report.wizard',
            'data': data,
            'report': report
        }
