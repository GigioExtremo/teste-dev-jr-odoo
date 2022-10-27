from dateutil.relativedelta import relativedelta
from odoo import api, fields, models


class OfferModel(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Model (Property Offer)"

    price = fields.Float(string="Price")
    status = fields.Selection(string="Status", nocopy=True,
                              selection=[("accepted", "Accepted"), ("refused", "Refused")])

    validity = fields.Integer(string="Validity", default=7)
    deadline_date = fields.Date(compute="_compute_deadline_date", inverse="_inverse_deadline_date",
                                string="Deadline Date")

    partner_id = fields.Many2one('res.partner', string="Buyer ID", required=True)
    property_id = fields.Many2one('estate.property', string="Property ID", required=True)

    # Computed methods

    @api.depends("validity", "create_date")
    def _compute_deadline_date(self):
        for record in self:
            if record.create_date:
                creation_date = record.create_date.date()
            else:
                creation_date = fields.Date.today()

            record.deadline_date = creation_date + relativedelta(days=record.validity)

    @api.depends("validity", "create_date")
    def _inverse_deadline_date(self):
        for record in self:
            if record.create_date:
                creation_date = record.create_date.date()
            else:
                creation_date = fields.Date.today()

            record.validity = abs((record.deadline_date - creation_date).days)
