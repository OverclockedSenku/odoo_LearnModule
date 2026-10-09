from odoo import fields, models


class EstimatedTimeWizard(models.TransientModel):
    _name = 'estimated.time.wizard'
    _description = 'Estimated Time Summary'

    product_qty = fields.Float(
        string='Manufacturing Quantity',
        readonly=True,
    )

    estimated_time = fields.Float(
        string='Time per Unit (Minutes)',
        readonly=True,
    )

    estimated_total_time = fields.Float(
        string='Total Estimated Time (Minutes)',
        readonly=True,
    )
