from odoo import http


class EventSnippet(http.Controller):

    @http.route(['/latest_events'], type="json", auth="public", methods=['POST'])
    def all_events(self):
        print('function controller')
        events = http.request.env['student.event'].search_read(
            [], ['name', 'image', 'id', 'venue'],
            order='create_date desc')
        print(events)

        return events
