# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Company(models.Model):
    _inherit = 'res.company'

    test_1 = fields.Char(string="test1")