# from odoo import http


# class MrpQaTracker(http.Controller):
#     @http.route('/mrp_qa_tracker/mrp_qa_tracker', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mrp_qa_tracker/mrp_qa_tracker/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mrp_qa_tracker.listing', {
#             'root': '/mrp_qa_tracker/mrp_qa_tracker',
#             'objects': http.request.env['mrp_qa_tracker.mrp_qa_tracker'].search([]),
#         })

#     @http.route('/mrp_qa_tracker/mrp_qa_tracker/objects/<model("mrp_qa_tracker.mrp_qa_tracker"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mrp_qa_tracker.object', {
#             'object': obj
#         })

