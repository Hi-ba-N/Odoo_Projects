# coding: utf-8
from odoo import models, api


class SchoolManagementClassReport(models.AbstractModel):
    _name = 'report.school_management.report_class'

    @api.model
    def _get_report_values(self, docids, data=None):
        print('check')
        query = """SELECT sl.name, sl.school_id, 
                   sr.name AS department_name     
                    FROM student_class sl
                     JOIN student_department sr ON sr.id = sl.department_id
                                  """

        params = []

        if data['department_id']:
            query += " AND sl.department_id IN %s"
            params.append(tuple(data['department_id']))

        self.env.cr.execute(query, params)
        report = self.env.cr.dictfetchall()
        print('rep', report)

        return {
            'doc_ids': docids,
            'doc_model': 'class.report.wizard',
            'data': data,
            'report': report
        }
