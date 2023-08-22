# -*- coding: utf-8 -*-
# from odoo import http


# class SystemAutomation(http.Controller):
#     @http.route('/system_automation/system_automation', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/system_automation/system_automation/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('system_automation.listing', {
#             'root': '/system_automation/system_automation',
#             'objects': http.request.env['system_automation.system_automation'].search([]),
#         })

#     @http.route('/system_automation/system_automation/objects/<model("system_automation.system_automation"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('system_automation.object', {
#             'object': obj
#         })
