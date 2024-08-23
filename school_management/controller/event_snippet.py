from odoo import http


class EventSnippet(http.Controller):

    @http.route(['/latest_events'], type="json", auth="public", methods=['POST'])
    def all_events(self):
        print('function controller')
        events = http.request.env['student.event'].search_read(
            [], ['name',  'venue'],
            order='create_date desc', limit=4)
        print(events)

        return events
