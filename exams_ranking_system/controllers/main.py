from odoo import http
from odoo.http import request

class Ranker(http.Controller):
    @http.route('/ranker/students/',website=True,auth='public')
    def ranker_results(self,**kw):
        return "Ranking"