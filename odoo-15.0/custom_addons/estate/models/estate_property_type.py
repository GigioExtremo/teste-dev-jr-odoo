from odoo import api, fields, models


class TypeModel(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Model (Property Type)"
    _order = "name"

    name = fields.Char(string="Name", required=True)
    sequence = fields.Integer(string="Sequence", default=1, help="Used to order stages. Lower is better.")

    property_ids = fields.One2many("estate.property", "property_type_id")
    offer_ids = fields.One2many("estate.property.offer", "property_type_id")
    offer_count = fields.Integer(compute="_compute_qty_offers")

    _sql_constraints = [
        ('estate_type_name_unique', 'UNIQUE(name)',
         'The name must be unique')
    ]

    # Computed Methods

    @api.depends('offer_ids')
    def _compute_qty_offers(self):
        for record in self:
            record.offer_count = len(record.offer_ids)