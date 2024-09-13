# coding: utf-8
from datetime import datetime

from dateutil.relativedelta import relativedelta

from odoo import Command, fields, models


class ProjectProject(models.Model):
    _inherit = 'project.project'

    month_line_ids = fields.One2many('project.date', 'project_id',
                                     string="Months")

    def action_schedule_date(self):
        schedule_dates = []
        today = datetime.now()
        year = today.year
        for month in range(1, 13):
            start_date = datetime(year, month, 1)
            end_date = start_date + relativedelta(months=1, days=-1)
            print(end_date)
            schedule_dates.append(Command.create({
                'month': start_date.strftime('%B'),
                'year': year,
                'from_date': start_date,
                'to_date': end_date,
            }))

            print(schedule_dates)
        self.write({'month_line_ids': schedule_dates})

