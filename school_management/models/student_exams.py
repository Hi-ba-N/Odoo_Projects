# coding: utf-8
from odoo import fields, models


class StudentExam(models.Model):
    """This  is used for Student exams"""
    _name = 'student.exams'
    _description = "Student Exam "
    _inherit = 'mail.thread'

    name = fields.Char('Name')
    class_id = fields.Many2one('student.class',
                               string='Class',
                               )
    paper_ids = fields.One2many('student.paper', 'exam_id', 'Paper')
    student_ids = fields.Many2many('student.registration',
                                   string='Student', domain="[ ('state', '=', 'registration')]")
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('assigned', 'Assigned'),
    ], string='Status', required=True, readonly=True,
        default='draft')

    def assign_exams(self):
        """This is used for assigning exam to student through button action"""
        self.student_ids = self.class_id.student_ids
        self.state = "assigned"





