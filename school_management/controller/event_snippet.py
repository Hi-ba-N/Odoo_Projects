from odoo import http
from odoo.http import request


class EventSnippet(http.Controller):

    @http.route(['/latest_events'], type="json", auth="public",
                methods=['POST'])
    def all_events(self):
        print('function')
        events = http.request.env['student.event'].sudo().search_read(
            [], ['name', 'image', 'id', 'venue', 'start_date'],
            order='create_date desc')
        # print(events)

        return events

    @http.route(['/event/view<int:id>'], type='http', auth='user', website=True)
    def get_event_data(self, **post):

        event = (request.env['student.event'].
                 browse(post.get('id')))
        print(event)
        return request.render('school_management.event_data_snippet',
                              {'event': event})
