# coding: utf-8
from datetime import datetime, timedelta, date

from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, Command
from odoo.exceptions import ValidationError


class StudentRegistration(models.Model):
    """This is for Student registration"""
    _name = "student.registration"
    _description = "Student"
    _inherit = 'mail.thread'
    _rec_name = 'first_name'

    sequence = fields.Char(default='New', readonly=True)
    first_name = fields.Char("First Name", required=True)
    last_name = fields.Char("Last Name", required=True)
    father = fields.Char("Father")
    mother = fields.Char("Mother")
    address = fields.Char("Communication Address")
    same_address = fields.Boolean("Same as Communication Address")
    permanent_address = fields.Char("Permanent Address")
    email = fields.Char('Email', required=True)
    phone = fields.Char("Phone", required=True)
    dob = fields.Date("DOB", required=True)
    age = fields.Char(compute="_compute_age", store=True)
    gender = fields.Selection(
        string='Gender',
        selection=[("female", "Female"), ("male", "Male")])
    registration_date = fields.Date("Registration Date",
                                    default=datetime.today())
    image = fields.Binary()
    school_id = fields.Many2one('res.company', string='School',
                                default=lambda self: self.env.company)
    department_id = fields.Many2one('student.department',
                                    string="Previous Department")
    previous_class_id = fields.Many2one('student.class',
                                        string="Previous Class")
    tc = fields.Binary(string="TC")
    aadhaar = fields.Char("Aadhaar")
    club_ids = fields.Many2many('student.club', string="Club")
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('registration', 'Registration'),
    ], string='Status', required=True, readonly=True,
        default='draft')
    exam_ids = fields.Many2many('student.exams', string="Exam", readonly=True)
    leave_ids = fields.One2many('student.leave', 'student_id',
                                string='Leaves')
    attendance = fields.Char(compute='_compute_attendance',
                             string='Attendance Status')
    student_class_id = fields.Many2one('student.class',

                                       string=" Class"

                                       )
    user_id = fields.Many2one('res.users', 'Users', readonly=True)

    _sql_constraints = [
        ('aadhaar_uniq', 'unique(aadhaar)',
         "Aadhar number must be unique"),
    ]

    def action_register(self):
        """This is used for button action to make class field required and changing the state to registration"""
        if not self.student_class_id:
            raise ValidationError("Class is required.")
        self.state = 'registration'
        # check = self.search(['|',
        #                      '&', ('first_name', '=', 'Farzeen'),
        #                      ('state', '=', 'draft'),
        #                      '&', ('first_name', '=', 'Athul'),
        #                      ('state', '=', 'registration')]
        #                     )
        #
        #
        # print(check.mapped('first_name'))

    @api.model
    def create(self, vals):
        """This is used for generating sequence number"""
        vals['sequence'] = self.env['ir.sequence'].next_by_code(
            'student_sequence')
        return super(StudentRegistration, self).create(vals)

    @api.depends('dob')
    def _compute_age(self):
        """This is  used for calculating age based on dob"""
        for record in self:
            if (record.dob and
                    record.dob <= fields.Date.today() - timedelta(days=1)):
                record.age = relativedelta(
                    fields.Date.from_string(fields.Date.today()),
                    fields.Date.from_string(record.dob)).years

            elif record.dob and record.dob >= fields.Date.today():
                record.age = relativedelta(
                    fields.Date.from_string(fields.Date.today()),
                    fields.Date.from_string(record.dob)).years
                record.age = 0

    @api.constrains('age')
    def check_age(self):
        """This is used for age validation"""
        for record in self:
            if record.age == '0':
                raise ValidationError(
                    "Choose valid dob")

    @api.depends('leave_ids.start_date', 'leave_ids.end_date')
    def _compute_attendance(self):
        """This is used for computing the student attendance based on the leave"""
        today = date.today()
        for record in self:
            absent_check = any(leave.start_date <= today <= leave.end_date
                               for leave in record.leave_ids)
            if absent_check:
                record.attendance = 'Absent'
            else:
                record.attendance = 'Present'

    def create_user(self):
        """This is used for create  student user"""
        print('user')
        user_vals = {
            'name': self.first_name,
            'login': self.email,
            'groups_id': [
                Command.link(
                    self.env.ref('school_management.group_student').id)]

        }
        new_user = self.env['res.users'].create(user_vals)
        self.user_id = new_user
