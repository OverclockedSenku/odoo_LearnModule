from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Test(models.Model):
    _inherit = "mrp.production"

    estimated_time = fields.Float(string='Estimated Time in Minutes',help='Estimated duration in minutes required to complete an unit production.')

    estimated_total_time = fields.Float(string='Total Estimated Time', compute='_compute_estimated_total_time', store=True)

    @api.depends('estimated_time', 'product_qty', 'product_id', 'product_id.product_tmpl_id.estimated_time_per_unit') 
    def _compute_estimated_total_time(self): 
        for order in self: 
            product_time = (
                order.product_id.product_tmpl_id.estimated_time_per_unit
                if order.product_id
                else 0
            )

            time_per_unit = (
                product_time
                if product_time > 0
                else order.estimated_time
                if order.estimated_time > 0
                else 10
            )
            order.estimated_total_time = ( time_per_unit * order.product_qty ) 

    @api.constrains('estimated_time')
    def _check_estimated_time(self):
        for order in self:
            if order.estimated_time < 0:
                raise ValidationError("Estimated time cannot be negative.")

    def action_show_estimated_time(self):
        self.ensure_one()

        product_time = (
            self.product_id.product_tmpl_id.estimated_time_per_unit
            if self.product_id
            else 0
        )
        
        time_per_unit = (
            product_time
            if product_time > 0
            else self.estimated_time
            if self.estimated_time > 0
            else 10
        )

        wizard = self.env['estimated.time.wizard'].create({
            'product_qty': self.product_qty,
            'estimated_time': time_per_unit,
            'estimated_total_time': time_per_unit * self.product_qty,
        })

        return {
            'type': 'ir.actions.act_window',
            'name': 'Estimated Time Summary',
            'res_model': 'estimated.time.wizard',
            'view_mode': 'form',
            'res_id': wizard.id,
            'target': 'new',
        }




class ProductTemplate(models.Model):
    _inherit = 'product.template'

    estimated_time_per_unit = fields.Float(
        string='Manufacturing Time per Unit (Minutes)',
        help='Estimated minutes required to manufacture one unit of this product.'
    )
