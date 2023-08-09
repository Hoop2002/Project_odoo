# -*- coding: utf-8 -*-
# from odoo import http


# class MainLineupMmc(http.Controller):
#     @http.route('/main_lineup_mmc/main_lineup_mmc', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/main_lineup_mmc/main_lineup_mmc/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('main_lineup_mmc.listing', {
#             'root': '/main_lineup_mmc/main_lineup_mmc',
#             'objects': http.request.env['main_lineup_mmc.main_lineup_mmc'].search([]),
#         })

#     @http.route('/main_lineup_mmc/main_lineup_mmc/objects/<model("main_lineup_mmc.main_lineup_mmc"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('main_lineup_mmc.object', {
#             'object': obj
#         })
