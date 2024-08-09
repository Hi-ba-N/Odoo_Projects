# coding: utf-8
from odoo import models, api


class SchoolManagementEventReport(models.AbstractModel):
    _name = 'report.school_management.report_event'

    @api.model
    def _get_report_values(self, docids, data=None):
        print('check')
        query = """SELECT sl.name, sl.description, sl.venue, 
                     sr.name AS club_name           
                    FROM student_event sl
                    JOIN student_club sr ON sr.id = sl.club_id
                                  """

        params = []

        if data['club_ids']:
            query += " AND sl.club_id IN %s"
            params.append(tuple(data['club_ids']))

        self.env.cr.execute(query, params)
        report = self.env.cr.dictfetchall()
        print(report)

        return {
            'doc_ids': docids,
            'doc_model': 'leave.report.wizard',
            'data': data,
            'report': report
        }
