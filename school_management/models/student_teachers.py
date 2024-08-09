# coding: utf-8
from odoo import fields, models


class StudentTeachers(models.Model):
    """This is used for student Teacher"""
    _name = "student.teachers"
    _description = "Teachers"
    _inherit = 'mail.thread'

    name = fields.Char("Name")
    email = fields.Char('Email', required=True)
    department_id = fields.Many2one('student.department',
                                    "Department")
