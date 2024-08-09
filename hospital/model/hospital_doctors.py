
from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    specialization = fields.Many2many('hospital.specialization', string="Specialization")


from odoo import models, api


class ReportStudentLeave(models.AbstractModel):
    _name = 'report.your_module.student_leave_report_template'
    _description = 'Student Leave Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        return {
            'doc_ids': docids,
            'doc_model': 'leave.report.wizard',
            'data': data,
            'report': data['report'],
        }





 # WHERE sl.start_date >= %s AND sl.end_date <= %s