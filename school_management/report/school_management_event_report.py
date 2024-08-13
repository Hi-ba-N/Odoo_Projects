# coding: utf-8
from datetime import date

from odoo import api, models
from odoo.exceptions import ValidationError


class SchoolManagementEventReport(models.AbstractModel):
    """This is event report abstract model"""
    _name = 'report.school_management.report_event'

    @api.model
    def _get_report_values(self, docids, data=None):
        """This is used  to get the report action and  return  its data"""
        print('check')
        query = """SELECT sl.id, sl.name, sl.start_date,sl.end_date, sl.venue, 
                     sr.name AS club_name ,sr.id as club_id          
                    FROM student_event sl
                    JOIN student_club sr ON sr.id = sl.club_id
                                  """

        params = []

        if data['club_ids']:
            query += " AND sl.club_id IN %s"
            params.append(tuple(data['club_ids']))
        if data['frequency'] == 'day':
            query += " where extract (day from start_date)= extract(day from current_date)"
        elif data['frequency'] == 'week':
            query += " where extract (week from start_date)= extract(week from current_date)"
        elif data['frequency'] == 'month':
            query += " where extract (month from start_date)= extract(month from current_date)"
        elif data['start_date'] and data['end_date']:
            query += " where start_date >= '%s' and end_date >= '%s'" % (
                data['start_date'], data['end_date'])
        elif data['start_date'] and not data['end_date']:
            query += "where start_date >= '%s' and end_date <= '%s'" % (
                data['start_date'], date.today())
            print(query)
        elif data['end_date'] and not data['start_date']:
            query += "where end_date <= '%s'" % (data['end_date'])

        self.env.cr.execute(query, params)
        report = self.env.cr.dictfetchall()

        if not report:
            print('no result')
            raise ValidationError("No related report found")
        print(report)

        return {
            # 'doc_ids': docids,
            'doc_model': 'leave.report.wizard',
            'data': data,
            'report': report
        }
