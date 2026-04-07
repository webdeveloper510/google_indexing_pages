# -*- coding: utf-8 -*-
# from odoo import http


# class GoogleIndexingPages(http.Controller):
#     @http.route('/google_indexing_pages/google_indexing_pages', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/google_indexing_pages/google_indexing_pages/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('google_indexing_pages.listing', {
#             'root': '/google_indexing_pages/google_indexing_pages',
#             'objects': http.request.env['google_indexing_pages.google_indexing_pages'].search([]),
#         })

#     @http.route('/google_indexing_pages/google_indexing_pages/objects/<model("google_indexing_pages.google_indexing_pages"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('google_indexing_pages.object', {
#             'object': obj
#         })

