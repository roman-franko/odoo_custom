# -*- coding: utf-8 -*-

from odoo import fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate properties"
    _order = "sequence"

    name = fields.Char(default="Unknown", required=True)
    description = fields.Char(default="Unknown")
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
    facades = fields.Integer(default=1)
    garage = fields.Boolean(default=False)
    garden = fields.Boolean(default=False)
    garden_area = fields.Integer(default=1)
    garden_orientation = fields.Char(default="Unknown")
    active = fields.Boolean('Active', default=False)
    sequence = fields.Integer('Sequence', default=10)

    user_id = fields.Many2one('res.users',
                              string='Salesperson',
                              default=lambda self: self.env.user)
    partner_id = fields.Many2one("res.partner", string="Buyer")

    tag_ids = fields.Many2many('estate.property.tag', string='Tags')
