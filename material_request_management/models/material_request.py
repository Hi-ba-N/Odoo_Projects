# coding: utf-8
from datetime import datetime

from odoo import api, fields, models, Command
from odoo.exceptions import ValidationError


class MaterialRequest(models.Model):
    """This model is used for viewing product quantity and price through wizard."""
    _name = 'material.request'
    _description = "Material Request"
    _rec_name = 'sequence'
    _inherit = 'mail.thread'

    sequence = fields.Char(default='New', readonly=True)
    employee_id = fields.Many2one('hr.employee', required=True, default=lambda
        self: self.env.user.employee_id, readonly=True)
    request_date = fields.Date('Request Date', default=datetime.today())
    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending_approval', 'Pending Approval'),
        ('manager_approved', 'Manager Approved'),
        ('head_approved', '  Approved'),
        ('rejected', 'Rejected')
    ], string='Status', default='draft', required=True)

    line_ids = fields.One2many('material.order.line', 'request_id',
                               string='Requested Items', required=True)
    rfq_count = fields.Integer(compute='_compute_count_rfq')
    transfer_count = fields.Integer(compute='_compute_count_transfer')

    @api.model
    def create(self, vals):
        """This is used for generating sequence number"""
        vals['sequence'] = self.env['ir.sequence'].next_by_code(
            'material_sequence')
        return super(MaterialRequest, self).create(vals)

    def action_confirm(self):
        """This is used for changing the state to pending approval through confirm button"""
        self.state = 'pending_approval'

    def action_approve_manager(self):
        """This is used for changing state to manager approved"""
        self.state = 'manager_approved'

    def action_approve_head(self):
        """This is used for creating rfq and internal transfer based on material request"""
        self.state = 'head_approved'
        for line in self.line_ids:
            print(self.line_ids.product_id.filtered(lambda x: not x.seller_ids))
            products = self.line_ids.product_id.filtered(
                lambda p: not p.seller_ids)

            print(products)
            if products:
                raise ValidationError(
                    "No vendor is available for " + str(
                        products.mapped('name')).strip("[]"))
            if line.material_action == 'purchase':
                purchase_vendor = line.product_id.seller_ids[0].partner_id
                line.env['purchase.order'].create({
                    'partner_id': purchase_vendor.id,
                    'origin': self.sequence,
                    'order_line': [Command.create({
                        'product_id': line.product_id.id,
                        'product_qty': line.quantity,

                    }
                    )],
                })
            else:
                line.env['stock.picking'].create({
                    'location_id': line.source_location_id.id,
                    'location_dest_id': line.destination_location_id.id,
                    'product_id': line.product_id.id,
                    'origin': self.sequence,
                    'picking_type_id': self.env.ref(
                        'stock.picking_type_internal').id,
                    'move_ids': [Command.create({
                        'name': '/',
                        'product_id': line.product_id.id,
                        'product_uom_qty': line.quantity,
                        'location_id': line.source_location_id.id,
                        'location_dest_id': line.destination_location_id.id,
                    })],
                })

    def action_reject(self):
        """This is used for changing the state to rejected"""
        self.state = 'rejected'

    def get_rfq(self):
        """This is used for getting rfq  detail"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'RFQ',
            'view_mode': 'tree',
            'res_model': 'purchase.order',
            'domain': [('origin', '=', self.sequence)],
            'context': "{'create': False}"
        }

    def get_transfer(self):
        """This is used for getting internal transfer detail"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Transfer',
            'view_mode': 'tree',
            'res_model': 'stock.picking',
            'domain': [('origin', '=', self.sequence)],
            'context': "{'create': False}"
        }

    def _compute_count_rfq(self):
        """This is used for counting rfq"""
        for record in self:
            record.rfq_count = self.env['purchase.order'].search_count(
                [('origin', '=', self.sequence)])

    def _compute_count_transfer(self):
        """This is used for counting transfer"""
        for record in self:
            record.transfer_count = self.env['stock.picking'].search_count(
                [('origin', '=', self.sequence)])
