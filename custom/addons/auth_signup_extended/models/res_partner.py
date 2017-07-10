# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import random
import werkzeug

from datetime import datetime, timedelta
from urlparse import urljoin

from odoo import api, fields, models, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    company_name = fields.Char(string='Company Name', copy=False)

