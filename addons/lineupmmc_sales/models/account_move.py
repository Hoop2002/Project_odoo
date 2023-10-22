# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from num2words import num2words
import math

class AccountMove(models.Model):
    _inherit = "account.move"

    def get_date(self):
        return datetime.now().strftime("%d.%m.%Y")
    
    def get_count_in_words(self, num):

        remains = int(str(num).split('.')[1])
        whole_count =  int(str(num).split('.')[0])



        return "{num_manat} manat, {num_gip} qəpik".format(
            num_manat=num2words(whole_count, lang="az"),
            num_gip=num2words(remains, lang="az")
        )
