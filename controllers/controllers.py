# -*- coding: utf-8 -*-
# from odoo import http


# class Upotussam(http.Controller):
#     @http.route('/upotussam/upotussam/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/upotussam/upotussam/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('upotussam.listing', {
#             'root': '/upotussam/upotussam',
#             'objects': http.request.env['upotussam.upotussam'].search([]),
#         })

#     @http.route('/upotussam/upotussam/objects/<model("upotussam.upotussam"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('upotussam.object', {
#             'object': obj
#         })
