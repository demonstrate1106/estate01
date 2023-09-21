from odoo import models, fields, api


class EstateProperty(models.Model):
    _inherit = 'real.estate'

    def action_solds(self):
        result = super(EstateProperty, self).action_solds()
        # partner_id = self.sale_buyer
        account_move = self.env['account.move'].create({
            'partner_id': self.sale_buyer,
            'move_type': 'out_invoice',
        })
        invoice_lines = []
        line_1 = {
            'name': self.name,
            'quantity': 1,
            'price_unit': self.price * 0.06,
        }
        invoice_lines.append((0, 0, line_1))
        line_2 = {
            'name': 'Administrative Fees',
            'quantity': 1,
            'price_unit': 100.00,
        }
        invoice_lines.append((0, 0, line_2))
        account_move.invoice_line_ids = invoice_lines
        return result
