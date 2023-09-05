# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class lineupmmc_sales(models.Model):
#     _name = 'lineupmmc_sales.lineupmmc_sales'
#     _description = 'lineupmmc_sales.lineupmmc_sales'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class Company(models.Model):
    _inherit = 'res.company'

    test_1 = fields.Char(string="test1")