# coding: utf-8
from odoo import http
from odoo.http import request


class LeaveForm(http.Controller):
    """This is for Leave Controller"""

    @http.route(['/leave'], type='http', website=True)
    def leave(self):
        """This is used searching leave record that is created through website and render  tree template"""
        data = request.env['student.leave'].sudo().search(
            [('is_website', '=', True)])

        values = {

            'record': data
        }

        return request.render("school_management.tmp_leave_tree", values)

    @http.route(['/leave/form'], type='http', website=True)
    def leave_form(self, leave_id=None):
        """This for rendering leave  form template"""

        leave = request.env['student.leave'].sudo().browse(
            int(leave_id)) if leave_id else None

        return request.render("school_management.tmp_leave_form",
                              {'leave': leave})

    @http.route(['/leave/form/submit'], type='http',
                website=True)
    def leave_form_submit(self, **post):
        """Creating leave through website"""
        leave = request.env['student.leave'].sudo().create({
            'student_id': post.get('student_id'),
            'start_date': post.get('start date'),
            'end_date': post.get('end date'),
            'reason': post.get('reason'),
            'is_website': True

        })

        return request.render(
            "school_management.tmp_leave_form_success")
