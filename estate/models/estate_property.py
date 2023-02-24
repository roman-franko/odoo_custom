# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class RecurringPlan(models.Model):
    _name = "estate.property"
    _description = "estate properties"
    _order = "sequence"

    name = fields.Char(default="Unknown", required=True)
    postcode = fields.Char(default="Unknown")
    postcode = fields.Char(default="Unknown")
    expected_price = fields.Float('Expected Price', required=True, default=2.1)
    selling_price = fields.Float('Selling Price', readonly=True)
    availability_date = fields.Date('Availability Date', 
                                    default=lambda self: fields.Datetime.add(
                                        fields.Datetime.now(),
                                        months=3
                                    ), 
                                    readonly=True, 
                                    copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(default=1)
    garage = fields.Boolean(default=False)
    garden = fields.Boolean(default=False)
    garden_area = fields.Integer(default=1)
    garden_orientation = fields.Char(default="Unknown")
    active = fields.Boolean('Active', default=False)
    sequence = fields.Integer('Sequence', default=10)