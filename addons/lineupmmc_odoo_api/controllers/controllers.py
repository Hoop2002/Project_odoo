# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, Response


class LineupmmcOdooApi(http.Controller):
    @http.route('/lineupmmc_odoo_api/lineupmmc_odoo_api', auth='public')
    def index(self, **kwargs):
        return "lineup mmc test api odoo"
