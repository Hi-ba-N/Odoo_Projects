# coding: utf-8
from odoo import models, api


class SchoolManagementClubReport(models.AbstractModel):
    _name = 'report.school_management.report_club'

    @api.model
    def _get_report_values(self, docids, data=None):
        print('check')
        query = """SELECT sl.name, sl.description, 
                   sr.first_name AS student_name     
                    FROM student_club sl
                     JOIN student_registration sr ON sr.id = sl.id
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
            'doc_model': 'club.report.wizard',
            'data': data,
            'report': report
        }
