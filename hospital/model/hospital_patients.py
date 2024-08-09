from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'
    age = fields.Integer("Age")
    blood_group = fields.Selection(
        string='Blood Group',
        selection=[("A+ve", "A +ve"), ("A-ve", "A-ve"), ("O+ve", "O+ve"), ("O-ve", "O-ve")])
    sequence = fields.Char("Sequence")
    gender = fields.Selection(
        string='Gender',
        selection=[("female", "Female"), ("male", "Male")])
    dob = fields.Date("DOB")

