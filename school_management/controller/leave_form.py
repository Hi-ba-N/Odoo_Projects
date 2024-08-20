from odoo import http
from odoo.http import request


class LeaveForm(http.Controller):

    @http.route(['/leave/'], type='http', website=True)
    def leave_form(self):
        return request.render("school_management.tmp_leave_form", {})


