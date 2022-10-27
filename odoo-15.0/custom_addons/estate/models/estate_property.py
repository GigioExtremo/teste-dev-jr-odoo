from dateutil.relativedelta import relativedelta
from odoo import api, fields, models


class ImmobileModel(models.Model):
    _name = "estate.property"
    _description = "Real Estate Model"

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(string="Title", default="Unknown", required=True)
    last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
    description = fields.Text(string="Description")

    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Available From",
                                    # default value: today's date plus 3 months
                                    default=lambda self: fields.Date.add(fields.Date.today(), relativedelta(months=+3)))

    expected_price = fields.Float(string="Expected Price", required=True)
    selling_price = fields.Float(string="Selling Price", readonly=True)
    state = fields.Selection(string="State",
                             selection=[("new", "New"), ("offer_received", "Offer Received"),
                                        ("offer_accepted", "Offer Accepted"),
                                        ("sold", "Sold"), ("canceled", "Canceled")], default="new")
    bedrooms = fields.Integer(string="Bedrooms", default=2)
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer(string="Facades")

    garage = fields.Boolean(string="Garage")

    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area (sqm)")
    garden_orientation = fields.Selection(string="Garden Orientation",
                                          selection=[("north", "North"), ("south", "South"), ("east", "East"),
                                                     ("west", "West")])

    total_area = fields.Integer(compute="_compute_total_area", string="Total Area (sqm)")

    # Relational fields

    property_type_id = fields.Many2one('estate.property.type', string="Property Type")
    property_type_name = fields.Char(string='Property Type Name', related='property_type_id.name', readonly=True,
                                     default=property_type_id.name)

    buyer_id = fields.Many2one('res.partner', string="Buyer", nocopy=True)
    buyer_name = fields.Char(string='Buyer Name', related='buyer_id.name', readonly=True)

    seller_id = fields.Many2one('res.users', string="Seller", default=lambda self: self.env.user)
    seller_name = fields.Char(string='Seller Name', related='seller_id.display_name', readonly=True)

    tags_ids = fields.Many2many("estate.property.tag", string="Tags")

    offers_ids = fields.One2many("estate.property.offer", "property_id")
    best_price = fields.Float(compute="_compute_best_price", string="Best Offer")

    # Computed Methods

    @api.depends('garden_area', 'living_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.garden_area + record.living_area

    @api.depends('offers_ids.price')
    def _compute_best_price(self):
        for record in self:
            if len(record.offers_ids) == 0:
                record.best_price = 0.0
            else:
                record.best_price = max([offer.price for offer in record.offers_ids])

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0
            self.garden_orientation = ''
