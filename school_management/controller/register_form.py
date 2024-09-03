# coding: utf-8
from odoo import http
from odoo.http import request


class RegisterForm(http.Controller):
    """This is for student form controller"""

    @http.route(['/register/', '/register/page/<int:page>'], type='http', auth='public',
                website=True)
    def register(self,page):
        """This is used searching student record that is created through website and render the tree template"""
        data = request.env['student.registration'].sudo().search(
            [('is_website', '=', True)])
        total_record = request.env['student.registration'].sudo().search_count(
            [('is_website', '=', True)])
        # print(total_record)
        pager = request.website.pager(
            url='/register/',
            total=total_record,
            page=page,
            step=3,
        )
        student_register = request.env['student.registration'].sudo().search(
            [('is_website', '=', True)], limit=3,
            offset=pager['offset'])
        print(student_register)
        values = {
            'record': data,
            'student_details': student_register,
            'pager': pager,
        }

        return request.render("school_management.tmp_register_tree", values)

    @http.route(['/register/form'], type='http', website=True,auth='public')
    def register_form(self, register_id=None):
        """This for rendering student register  form template"""

        student = request.env['student.registration'].sudo().browse(
            int(register_id)) if register_id else None
        return request.render("school_management.tmp_register_form",
                              {'student': student})

    @http.route(['/register/form/submit'], type='http',
                website=True,auth='public')
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

        return request.render("school_management.tmp_register_form_success",
                              )
