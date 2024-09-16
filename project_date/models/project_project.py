# coding: utf-8
from datetime import datetime

from dateutil.relativedelta import relativedelta

from odoo import Command, fields, models


class ProjectProject(models.Model):
    _inherit = 'project.project'

    month_line_ids = fields.One2many('project.date', 'project_id',
                                     string="Months")

    def action_schedule_date(self):
        """ This Action button will add 12 lines to the O2m field. which contains the current year's details """
        schedule_dates = []
        today = datetime.now()
        year = today.year
        for month in range(1, 13):
            start_date = datetime(year, month, 1)
            end_date = start_date + relativedelta(months=1, days=-1)
            start_day = start_date.strftime("%A")
            end_day = end_date.strftime("%A")
            print(start_day)
            print(end_day)
            schedule_dates.append(Command.create({
                'month': start_date.strftime('%B'),
                'year': year,
                'from_date': start_date,
                'to_date': end_date,
                'start_day': start_day,
                'end_day': end_day
            }))

            print(schedule_dates)
        self.write({'month_line_ids': schedule_dates})

