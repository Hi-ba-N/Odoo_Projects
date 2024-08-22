from odoo import http


class ElearningSnippet(http.Controller):

    @http.route(['/latest_elearning_courses'], type="json", auth="public")
    def all_courses(self):
        events = http.request.env['student.event'].search_read(
            [], ['name', 'image', 'venue'],
            order='create_date desc', limit=10)
        print(events)

        return events
