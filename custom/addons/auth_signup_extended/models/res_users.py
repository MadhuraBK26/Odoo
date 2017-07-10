# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from ast import literal_eval

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.tools.misc import ustr

from odoo.addons.base.ir.ir_mail_server import MailDeliveryException
from odoo.addons.auth_signup.models.res_partner import SignupError, now


class ResUsers(models.Model):
    _inherit = 'res.users'

    company_name = fields.Char(string='Company Name', copy=False)
    phone = fields.Char(string='Phone', copy=False)
    country_id = fields.Many2one('res.country', string='Country', copy=False)
