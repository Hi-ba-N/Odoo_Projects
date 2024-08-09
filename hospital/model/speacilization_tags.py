
from odoo import models, fields


class HospitalSpecialization(models.Model):
    _name = "hospital.specialization"
    name = fields.Char("Name")
