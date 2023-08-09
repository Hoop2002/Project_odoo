# -*- coding: utf-8 -*-
# from odoo import http


# class ContractLineupMmc(http.Controller):
#     @http.route('/contract_lineup_mmc/contract_lineup_mmc', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contract_lineup_mmc/contract_lineup_mmc/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('contract_lineup_mmc.listing', {
#             'root': '/contract_lineup_mmc/contract_lineup_mmc',
#             'objects': http.request.env['contract_lineup_mmc.contract_lineup_mmc'].search([]),
#         })

#     @http.route('/contract_lineup_mmc/contract_lineup_mmc/objects/<model("contract_lineup_mmc.contract_lineup_mmc"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contract_lineup_mmc.object', {
#             'object': obj
#         })
