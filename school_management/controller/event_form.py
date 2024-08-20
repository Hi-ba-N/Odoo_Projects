from odoo import http
from odoo.http import request


class EventForm(http.Controller):

    @http.route(['/event/'], type='http', website=True)
    def event_form(self):
        return request.render("school_management.tmp_leave_form", {})

