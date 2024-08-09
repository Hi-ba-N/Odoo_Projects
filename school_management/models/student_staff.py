# coding: utf-8
from odoo import fields, models


class StudentStaff(models.Model):
    """This is used for student Staff"""
    _name = "student.staff"
    _description = "Staff"
    _inherit = 'mail.thread'

    name = fields.Char("Name")
    email = fields.Char('Email', required=True)
    department_id = fields.Many2one('student.department',
                                    "Department")

