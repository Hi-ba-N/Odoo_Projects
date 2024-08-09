# coding: utf-8
from odoo import fields, models


class StudentAcademic(models.Model):
    """this  is used for Academic year"""
    _name = 'student.academic'
    _description = "Student Academic Year"
    _inherit = 'mail.thread'

    name = fields.Char("Name")

