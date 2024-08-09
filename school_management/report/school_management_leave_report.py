# coding: utf-8
from datetime import date

from odoo import models, api


class SchoolManagementLeaveReport(models.AbstractModel):
    _name = 'report.school_management.report_leave'

    @api.model
    def _get_report_values(self, docids, data=None):
        print('check')
        query = """SELECT sl.start_date, sl.end_date, sl.total_days, sl.reason,
                                         sr.first_name AS student_name, sc.name AS class_name
                                  FROM student_leave sl
                                  JOIN student_registration sr ON sr.id = sl.student_id
                                  JOIN student_class sc ON sc.id = sr.student_class_id
                    
                                  """
        # bcd = 'world'
        # abc = 'hello %s' % bcd
        # abc = f'hello {bcd}'
        params = []

        if data['class_ids']:
            query += " AND sr.student_class_id IN %s"
            params.append(tuple(data['class_ids']))

        elif data['student_ids']:
            query += " AND sl.student_id IN %s"
            params.append(tuple(data['student_ids']))
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
        print(report)

        return {
            'doc_ids': docids,
            'doc_model': 'leave.report.wizard',
            'data': data,
            'report': report
        }
