# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare, float_is_zero

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate properties"
    _order = "sequence"

    name = fields.Char(default="Unknown", required=True)
    description = fields.Char(default="Unknown")
    state = fields.Char('Status', readonly=True)
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
    active = fields.Boolean('Active', default=True)
    sequence = fields.Integer('Sequence', default=10)

    user_id = fields.Many2one('res.users',
                              string='Salesperson',
                              default=lambda self: self.env.user)
    partner_id = fields.Many2one("res.partner", string="Buyer")

    tag_ids = fields.Many2many('estate.property.tag', string='Tags')
    offer_ids = fields.One2many(
        "estate.property.offer", "property_id", string="Offers")

    total_area = fields.Char(compute="_compute_total_area")

    _sql_constraints = [
        ('expected_price_positive',
         'CHECK(expected_price > 0)',
         'A expected price must be strictly positive!'),

        ('selling_price_positive', 'CHECK(selling_price >= 0)',
         'A selling price  must be positive!')
    ]

    @api.constrains('selling_price', 'expected_price')
    def _check_selling_price(self):
        for record in self:
            if not float_is_zero(record.selling_price, precision_digits=2) and not float_is_zero(record.expected_price, precision_digits=2) and float_compare(record.selling_price/record.expected_price, 0.9, precision_digits=2) < 0:
                raise ValidationError(
                    'The selling price cannot be lower than 90% of the expected price')

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'North'
        else:
            self.garden_area = 0
            self.garden_orientation = ''

    def sold(self):
        for record in self:
            if record.state != 'Canceled' and record.state != 'Sold':
                record.state = 'Sold'
            else:
                raise UserError(
                    "You can't sold a property that is already sold or canceled")
        return True

    def cancel(self):
        for record in self:
            if record.state != 'Canceled' and record.state != 'Sold':
                record.state = 'Canceled'
            else:
                raise UserError(
                    "You can't cancel a property that is already sold or canceled")
        return True

    def set_buyer(self, partner_id):
        for record in self:
            record.partner_id = partner_id
        return True

    def set_selling_price(self, selling_price):
        for record in self:
            record.selling_price = selling_price
        return True

    def has_active_offer(self):
        for record in self:
            for offer in record.offer_ids:
                if offer.status == 'Accepted':
                    return True
        return False
