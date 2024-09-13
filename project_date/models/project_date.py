# coding: utf-8
from odoo import models, fields


class ProjectDate(models.Model):
    _name = 'project.date'
    _description = 'Project Date'

    project_id = fields.Many2one('project.project', string="Project")
    month = fields.Char("Month", readonly=True)
    year = fields.Char(string="Year", readonly=True)
    from_date = fields.Date(string="Start Date", readonly=True)
    to_date = fields.Date(string="End Date", readonly=True)
