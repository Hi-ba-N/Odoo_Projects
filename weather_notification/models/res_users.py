# coding: utf-8
import requests

from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    api_key = fields.Char('Weather Api Key')
    city = fields.Char('City')

    def get_current_weather(self):
        """Fetch current weather using OpenWeatherMap API."""
        self.ensure_one()
        api_url = "https://api.openweathermap.org/data/2.5/weather"
        values = {
            'city': self.city,
            'appid': self.api_key,

        }
        response = requests.get(api_url,values)
        weather_data = response.json()
        print(weather_data)



