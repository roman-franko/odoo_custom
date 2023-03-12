# -*- coding: utf-8 -*-

from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "estate property type"

    name = fields.Char(default="Unknown", required=True)

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'This name is already exising!'),
    ]
