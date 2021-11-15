# Copyright 2021 Kevin MASSON
# License AGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

# from odoo import fields, models
from openerp import models
from openerp.addons.cmis_field import fields


class CrmClaim(models.Model):
    _inherit = 'crm.claim'

    cmis_folder = fields.CmisFolder()
