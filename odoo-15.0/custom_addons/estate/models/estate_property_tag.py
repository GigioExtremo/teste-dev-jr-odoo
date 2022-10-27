from odoo import fields, models


class TagModel(models.Model):
    _name = "estate.property.tag"
    _description = "Real Estate Model (Property Tag)"

    name = fields.Char(string="Name", required=True)
