# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo-debranding-addon-v15(http.Controller):
#     @http.route('/odoo-debranding-addon-v15/odoo-debranding-addon-v15', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo-debranding-addon-v15/odoo-debranding-addon-v15/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo-debranding-addon-v15.listing', {
#             'root': '/odoo-debranding-addon-v15/odoo-debranding-addon-v15',
#             'objects': http.request.env['odoo-debranding-addon-v15.odoo-debranding-addon-v15'].search([]),
#         })

#     @http.route('/odoo-debranding-addon-v15/odoo-debranding-addon-v15/objects/<model("odoo-debranding-addon-v15.odoo-debranding-addon-v15"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo-debranding-addon-v15.object', {
#             'object': obj
#         })
