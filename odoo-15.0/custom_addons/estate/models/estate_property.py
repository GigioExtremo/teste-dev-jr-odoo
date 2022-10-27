from dateutil.relativedelta import relativedelta
from odoo import fields, models


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
                                    default=lambda self: fields.Date.add(fields.Date.today(), relativedelta(+3)))

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

    property_type_id = fields.Many2one('estate.property.type', string="Property Type")
    property_type_name = fields.Char(string='Property Type Name', related='property_type_id.name', readonly=True,
                                     default=property_type_id.name)

    buyer_id = fields.Many2one('res.partner', string="Buyer", nocopy=True)
    buyer_name = fields.Char(string='Buyer Name', related='buyer_id.name', readonly=True)

    seller_id = fields.Many2one('res.users', string="Seller", default=lambda self: self.env.user)
    seller_name = fields.Char(string='Seller Name', related='seller_id.display_name', readonly=True)

    tags_ids = fields.Many2many("estate.property.tag", string="Tags")

    offers_ids = fields.One2many("estate.property.offer", "property_id")
