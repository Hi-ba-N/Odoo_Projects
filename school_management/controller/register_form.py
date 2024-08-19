from odoo import http
from odoo.http import request


class RegisterForm(http.Controller):

    @http.route(['/register/'], type='http', website=True)
    def register_form(self):
        return request.render("school_management.tmp_register_form", {})

    @http.route(['/register/form/submit'], type='http', auth="public",
                website=True)
    def register_form_submit(self, **post):
        student = request.env['student.registration'].sudo().create({
            'first_name': post.get('first_name'),
            'last_name': post.get('last_name'),
            'email': post.get('email'),
            'phone': post.get('phone'),
            'dob': post.get('dob'),

        })
        vals = {
            'student': student,
        }

        return request.render(
            "school_management.tmp_register_form_success", vals)
