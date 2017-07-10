# -*- coding: utf-8 -*-
# (c) 2015 Antiun Ingeniería S.L. - Sergio Teruel
# (c) 2015 Antiun Ingeniería S.L. - Carlos Dauden
# © 2016 Jairo Llopis <jairo.llopis@tecnativa.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp.addons.auth_signup.controllers.main import AuthSignupHome
from openerp.http import request


class AuthSignupHome(AuthSignupHome):

##    @http.route('/web/signup', type='http', auth='public', website=True)
##    def web_auth_signup(self, *args, **kw):
##        qcontext = self.get_auth_signup_qcontext()
##        qcontext['country_id'] = request.env['res.country'].sudo().search([])
##        if not qcontext.get('token') and not qcontext.get('signup_enabled'):
##            raise werkzeug.exceptions.NotFound()
##
##        if 'error' not in qcontext and request.httprequest.method == 'POST':
##            try:
##                self.do_signup(qcontext)
##                return super(AuthSignupHome, self).web_login(*args, **kw)
##            except (SignupError, AssertionError), e:
##                if request.env["res.users"].sudo().search([("login", "=", qcontext.get("login"))]):
##                    qcontext["error"] = _("Another user is already registered using this email address.")
##                else:
##                    _logger.error(e.message)
##                    qcontext['error'] = _("Could not create a new account.")
##
##        return request.render('auth_signup.signup', qcontext)


    def do_signup(self, qcontext):
        """ Shared helper that creates a res.partner out of a token """
        values = { key: qcontext.get(key) for key in ('login', 'name', 'password', 'phone', 'company_name', 'country_id') }
        assert values.values(), "The form was not properly filled in."
        assert values.get('password') == qcontext.get('confirm_password'), "Passwords do not match; please retype them."
        supported_langs = [lang['code'] for lang in request.env['res.lang'].sudo().search_read([], ['code'])]
        if request.lang in supported_langs:
            values['lang'] = request.lang
        self._signup_with_values(qcontext.get('token'), values)
        request.env.cr.commit()
