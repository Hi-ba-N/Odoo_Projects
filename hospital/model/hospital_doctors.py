
from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    specialization = fields.Many2many('hospital.specialization', string="Specialization")



 # WHERE sl.start_date >= %s AND sl.end_date <= %s
# < odoo >
# < template
# id = "assets_frontend"
# inherit_id = "web.assets_frontend"
# name = "Leave Form Assets" >
# < xpath
# expr = "."
# position = "inside" >
# < script
# type = "text/javascript"
# src = "/school_management/static/src/js/leave_days_calculator.js" / >
# < / xpath >
# < / template >
# < / odoo >