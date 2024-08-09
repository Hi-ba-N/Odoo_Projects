# coding: utf-8
from odoo import fields, models


class StudentSubject(models.Model):
    """This is used for subject"""
    _name = "student.subject"
    _description = "Student Subject"
    _inherit = 'mail.thread'

    name = fields.Char("Name")
    department_id = fields.Many2one('student.department', "Department")
