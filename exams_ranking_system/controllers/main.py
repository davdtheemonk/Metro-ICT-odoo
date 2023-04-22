from odoo import http
from odoo.http import request

class Ranker(http.Controller):
    @http.route('/ranker/students/',website=True,auth='public')
    def ranker_results(self,**kw):
        return request.render("exams_ranking_system.exam_ranking_table",{})