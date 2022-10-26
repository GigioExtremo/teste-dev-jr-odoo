from dateutil.relativedelta import relativedelta
from odoo import fields, models


class TestModel(models.Model):
    _name = "estate.property"
    _description = "Real Estate Model"

    active = fields.Boolean(string="active", default=True)
    name = fields.Char(string="name", default="Unknown", required=True)
    last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
    description = fields.Text(string="description")
    postcode = fields.Char(string="postcode")
    date_availability = fields.Date(string="date_availability",
                                    # default value: today's date plus 3 months
                                    default=lambda self: fields.Date.add(fields.Date.today(), relativedelta(+3)))
    expected_price = fields.Float(string="expected_price", required=True)
    selling_price = fields.Float(string="selling_price")
    state = fields.Selection(string="state",
                             selection=[("new", "New"), ("offer_received", "Offer Received"),
                                        ("offer_accepted", "Offer Accepted"),
                                        ("sold", "Sold"), ("canceled", "Canceled")], default="new")
    bedrooms = fields.Integer(string="bedrooms", default=2)
    living_area = fields.Integer(string="living_area")
    facades = fields.Integer(string="facades")
    garage = fields.Boolean(string="garage")
    garden = fields.Boolean(string="garden")
    garden_area = fields.Integer(string="garden_area")
    garden_orientation = fields.Selection(string="garden_orientation",
                                          selection=[("north", "North"), ("south", "South"), ("east", "East"),
                                                     ("west", "West")])
