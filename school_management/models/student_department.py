# coding: utf-8
from odoo import fields, models


class StudentDepartment(models.Model):
    """This is for  Student department"""
    _name = "student.department"
    _description = "Student Department"
    _inherit = 'mail.thread'

    name = fields.Char(string="Name")
    head_of_department_id = fields.Many2one('res.partner',
                                            string="Head of Department")
