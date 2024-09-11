

from odoo import models, fields, api


class HospitalOp(models.Model):
    _name = "hospital.op"
    sequence = fields.Char("Sequence")
    date = fields.Date("Date", default=fields.Date.today())
    patient_name = fields.Many2one('res.partner', string="Patients")
    age = fields.Integer(related="patient_name.age")
    blood_group = fields.Selection(related="patient_name.blood_group")

    doctor_id = fields.Many2one('hr.employee', string="Doctor")
    ticket_number = fields.Integer("Token Number")
    currency_id = fields.Many2one("res.currency")
    fees = fields.Monetary(related="doctor_id.hourly_cost", string="Fee", currency_field="currency_id")

    @api.model
    def create(self, vals):
        vals['sequence'] = self.env['ir.sequence'].next_by_code('my_sequence_code')
        return super(HospitalOp, self).create(vals)

    # self._context.get('active_id').
    # self.env['sale.order'].browse(self._context.get('active_ids')).user_id.

    # print("workdksm")
    # check=self.env['sale.order'].search([('amount_total', '>=', 500)]).read(['partner_id','name','amount_total'])
    # print(check)

    # from odoo import http
    # from odoo.http import request
    #
    # class WeatherController(http.Controller):
    #
    #     @http.route('/get_weather_info', type='json', auth="user")
    #     def get_weather_info(self):
    #         user = request.env.user
    #         return {
    #             'city': user.city,  # Assuming you added a 'city' field to res.users
    #             'apiKey': user.api_key,  # Assuming you added an 'api_key' field to res.users
    #         }


