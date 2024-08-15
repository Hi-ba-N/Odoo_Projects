
from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    specialization = fields.Many2many('hospital.specialization', string="Specialization")



 # WHERE sl.start_date >= %s AND sl.end_date <= %s