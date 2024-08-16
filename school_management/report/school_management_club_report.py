# coding: utf-8
from odoo import api, models
from odoo.exceptions import ValidationError


class SchoolManagementClubReport(models.AbstractModel):
    """This is club report abstract model"""
    _name = 'report.school_management.report_club'

    @api.model
    def _get_report_values(self, docids, data=None):
        """This is used  to get the report action and  return  its data"""
        print('check')
        query = """ """

        params = []
        print(data['club_ids'])
        if data['student_ids']:
            print('condition')
            query = """SELECT sr.first_name AS student_name, sc.name AS club_name,sc.id AS club_id,sq.name as class_name
                    FROM student_registration sr
                    JOIN student_club_student_registration_rel sp ON sr.id = student_registration_id
                    JOIN student_club sc ON sc.id = student_club_id
                    Join student_class sq on sr.id = student_class_id
                    where sr.id IN %s"""
            # query += " AND sl.id IN %s"
            print(query)
            params.append(tuple(data['student_ids']))
        elif data['club_ids']:

            query = """SELECT sc.id AS club_id, sc.name AS club_name, sr.first_name AS student_name
                    FROM student_club sc
                    JOIN student_club_student_registration_rel sp ON sc.id = student_club_id
                    JOIN student_registration sr ON sr.id = sp.student_registration_id
                    where sc.id IN %s
                    """
            print(query)

            params.append(tuple(data['club_ids']))

        self.env.cr.execute(query, params)

        report = self.env.cr.dictfetchall()

        print(report)

        return {
            'doc_ids': docids,
            'doc_model': 'club.report.wizard',
            'data': data,
            'report': report
        }
