
from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    specialization = fields.Many2many('hospital.specialization', string="Specialization")



 # WHERE sl.start_date >= %s AND sl.end_date <= %s
# <div class="backtosnippet">
# <a href="/" class="reverse_link">Back</a>
# </div>



    # @http.route(['/room/<int:id>'], type='http', auth='user', website=True)
    # def get_room_data(self, **post):
    #     room = (request.env['hostel.room'].
    #             browse(post.get('id')))
    #     return request.render('hostel_management.room_data_snippet',
    #                          {'room':room})