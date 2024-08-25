# coding: utf-8
from odoo import http
from odoo.http import request


class EventForm(http.Controller):
    """This is for Event Controller"""

    @http.route(['/event/'], type='http', website=True)
    def event(self):
        """This is used searching event record that is created through website and render  tree template"""
        data = request.env['student.event'].sudo().search(
            [('is_website', '=', True)])

        values = {
            'record': data
        }
        return request.render("school_management.tmp_event_tree", values)

    @http.route(['/event/form'], type='http', website=True)
    def event_form(self, event_id=None):
        """This for rendering event form template"""
        event = request.env['student.event'].sudo().browse(
            int(event_id)) if event_id else None

        # print(event)

        return request.render("school_management.tmp_event_form",
                              {'event': event})

    @http.route(['/event/submit'], type='http',
                website=True)
    def event_form_submit(self, **post):
        """Creating event through website"""
        event = request.env['student.event'].sudo().create({
            'name': post.get('event'),
            'club_id': post.get('club'),
            'start_date': post.get('start date'),
            'end_date': post.get('end date'),
            'is_website': True

        })
        print(event)
        return request.render("school_management.tmp_event_form_success")
