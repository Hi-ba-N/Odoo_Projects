# coding: utf-8
from odoo import http
from odoo.http import request


class RegisterForm(http.Controller):
    """This is for student form controller"""
    @http.route(['/register/'], type='http', website=True)
    def register(self):
        """This is used searching student record that is created through website and render the tree template"""
        data = request.env['student.registration'].sudo().search([('is_website', '=', True)])
        print(data)
        values = {
            'record': data
        }

        return request.render("school_management.tmp_register_tree", values)

    @http.route(['/register/form'], type='http', website=True)
    def register_form(self):
        """This for rendering student register  form template"""
        return request.render("school_management.tmp_register_form")

    @http.route(['/register/form/submit'], type='http',
                website=True)
    def register_form_submit(self, **post):
        """Creating student through website"""
        student = request.env['student.registration'].sudo().create({
            'first_name': post.get('first_name'),
            'last_name': post.get('last_name'),
            'email': post.get('email'),
            'phone': post.get('phone'),
            'dob': post.get('dob'),
            'is_website': True

        })

        vals = {
            'student': student,
        }
        return request.render("school_management.tmp_register_form_success",
                              vals)
