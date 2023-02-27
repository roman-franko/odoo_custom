# -*- coding: utf-8 -*-

from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "estate property type"
    # _order = "sequence"

    name = fields.Char(default="Unknown", required=True)
