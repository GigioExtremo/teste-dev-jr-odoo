from odoo import fields, models


class TypeModel(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Model (Property Type)"

    name = fields.Char(string="Name", required=True)
