# -*- coding: utf-8 -*-

from odoo import fields, models


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "estate property tag"

    name = fields.Char(default="Unknown", required=True)

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'This name is already exising!'),
    ]
