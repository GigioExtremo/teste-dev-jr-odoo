from odoo import models, Command


class EstateInheritedModel(models.Model):
    _inherit = "estate.property"

    def sell_property(self):
        partner_id = self.buyer_id
        move_type = 'out_invoice'  # Customer Invoice
        journal_id = self.env['account.move'].with_context(default_move_type=move_type)._get_default_journal().id

        property_name = self.name
        property_value_6pct = self.selling_price * 0.06

        account_move_creation_dict = {
            'partner_id': partner_id,
            'move_type': move_type,
            'journal_id': journal_id,
            'invoice_line_ids': [
                # Normal invoice line
                Command.create({
                    "name": property_name,
                    "quantity": 1,
                    "price_unit": property_value_6pct
                }),
                # Administrative Fee of 100.00
                Command.create({
                    "name": "Administrative fees",
                    "quantity": 1,
                    "price_unit": 100.00
                })
            ]
        }

        self.env['account.move'].create(account_move_creation_dict)

        return super().sell_property()

# move_type = fields.Selection(selection=[
#            ('entry', 'Journal Entry'),
#            ('out_invoice', 'Customer Invoice'),
#            ('out_refund', 'Customer Credit Note'),
#            ('in_invoice', 'Vendor Bill'),
#            ('in_refund', 'Vendor Credit Note'),
#            ('out_receipt', 'Sales Receipt'),
#            ('in_receipt', 'Purchase Receipt')
