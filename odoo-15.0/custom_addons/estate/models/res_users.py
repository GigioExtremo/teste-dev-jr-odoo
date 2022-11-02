from odoo import fields, models


class Users(models.Model):
    _inherit = 'res.users'

    properties_ids = fields.One2many(
        'estate.property', 'seller_id', 'Properties to Sell',
        domain=lambda self: "['|', ('state', '=', 'new'), ('state', '=', 'offer_received')]")
