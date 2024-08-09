# coding: utf-8
from odoo import fields, models


class StudentPaper(models.Model):
    """This is used for managing student exam papers"""
    _name = "student.paper"
    _description = "Paper"
    _rec_name = "subject_id"
    _inherit = 'mail.thread'

    subject_id = fields.Many2one('student.subject', string="Subject")
    pass_mark = fields.Integer('Pass mark')
    max_mark = fields.Integer("Total")
    exam_id = fields.Many2one('student.exams', string='Exam')
