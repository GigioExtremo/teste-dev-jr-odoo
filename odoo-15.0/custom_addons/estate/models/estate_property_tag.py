from random import randint

from odoo import fields, models


class TagModel(models.Model):
    _name = "estate.property.tag"
    _description = "Real Estate Model (Property Tag)"
    _order = "name"

    def _default_color(self):
        return randint(1, 11)

    name = fields.Char(string="Name", required=True)

    color = fields.Integer(string="Color", default=lambda self: self._default_color())

    _sql_constraints = [
        ('estate_tag_name_unique', 'UNIQUE(name)',
         'The name must be unique')
    ]
