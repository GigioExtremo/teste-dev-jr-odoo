from odoo import fields, models


class TypeModel(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Model (Property Type)"
    _sql_constraints = [
        ('estate_type_name_unique', 'UNIQUE(name)',
         'The name must be unique')
    ]

    name = fields.Char(string="Name", required=True)
