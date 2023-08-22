# -*- coding: utf-8 -*-
# from odoo import http


# class LineupmmcSales(http.Controller):
#     @http.route('/lineupmmc_sales/lineupmmc_sales', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lineupmmc_sales/lineupmmc_sales/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lineupmmc_sales.listing', {
#             'root': '/lineupmmc_sales/lineupmmc_sales',
#             'objects': http.request.env['lineupmmc_sales.lineupmmc_sales'].search([]),
#         })

#     @http.route('/lineupmmc_sales/lineupmmc_sales/objects/<model("lineupmmc_sales.lineupmmc_sales"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lineupmmc_sales.object', {
#             'object': obj
#         })
