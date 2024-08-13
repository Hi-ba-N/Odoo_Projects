# coding: utf-8
from odoo import models, api
from odoo.exceptions import ValidationError


class SchoolManagementClassReport(models.AbstractModel):
    """This is class report abstract model"""
    _name = 'report.school_management.report_class'

    @api.model
    def _get_report_values(self, docids, data=None):
        """This is used  to get the report action and  return  its data"""

        print('check')
        query = """SELECT sl.name as class_name, sl.id as class_id,
                   sr.name AS department_name,
                   st.first_name AS student_name
                    FROM student_class sl
                     JOIN student_department sr ON sr.id = sl.department_id
                     JOIN student_registration st ON st.student_class_id = sl.id
                                  """

        params = []

        if data['department_id']:
            query += " AND sl.department_id IN %s"
            params.append(tuple(data['department_id']))
        elif data['class_ids']:
            query += " AND st.student_class_id IN %s"
            params.append(tuple(data['class_ids']))

        self.env.cr.execute(query, params)
        report = self.env.cr.dictfetchall()
        if not report:
            print('no result')
            raise ValidationError("No related report found")
        print('rep', report)

        return {
            'doc_ids': docids,
            'doc_model': 'class.report.wizard',
            'data': data,
            'report': report
        }
