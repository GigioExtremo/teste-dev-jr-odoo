from dateutil.relativedelta import relativedelta
from odoo import api, fields, models
from odoo.exceptions import UserError


class OfferModel(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Model (Property Offer)"

    price = fields.Float(string="Expected Price")
    status = fields.Selection(string="Status", nocopy=True,
                              selection=[("accepted", "Accepted"), ("refused", "Refused")], readonly=True)

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

    def accept_offer(self):
        for record in self:
            if record.status == 'accepted':
                continue

            if record.property_id.state == 'offer_accepted':
                raise UserError("Another offer was already accepted.")
            if record.status == "refused":
                raise UserError("The offer was already refused.")
            if record.property_id.state == "sold":
                raise UserError('The property was sold already.')
            if record.property_id.state == "canceled":
                raise UserError('The property sale was canceled.')

            record.status = "accepted"
            record.property_id.state = 'offer_accepted'
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.partner_id

        return True

    def deny_offer(self):
        for record in self:
            if record.property_id.state == "canceled":
                raise UserError('The property sale was canceled.')
            if record.status == "accepted":
                raise UserError("The offer was already accepted.")

            record.status = "refused"
        return True
