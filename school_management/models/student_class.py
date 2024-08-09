# coding: utf-8
from odoo import fields, models


class StudentClass(models.Model):
    """This is used for student class"""
    _name = "student.class"
    _description = "Student Class"
    _inherit = 'mail.thread'

    name = fields.Char("Name")
    department_id = fields.Many2one('student.department',
                                    "Department")
    head_of_department_id = fields.Many2one(
        string='Head of Department',
        related='department_id.head_of_department_id')
    school_id = fields.Many2one('res.company', string='School',
                                default=lambda self: self.env.company)
    student_ids = fields.One2many('student.registration', 'student_class_id', string='Student')
