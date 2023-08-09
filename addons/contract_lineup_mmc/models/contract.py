from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class ContractContract(models.Model):

    _inherit = "contract.contract"

    