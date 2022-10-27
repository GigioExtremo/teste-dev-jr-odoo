from odoo import fields, models


class OfferModel(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Model (Property Offer)"

    price = fields.Float(string="Price")
    status = fields.Selection(string="Status", nocopy=True,
                              selection=[("accepted", "Accepted"), ("refused", "Refused")])

    partner_id = fields.Many2one('res.partner', string="Buyer ID", required=True)
    property_id = fields.Many2one('estate.property', string="Property ID", required=True)
