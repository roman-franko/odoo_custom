# -*- coding: utf-8 -*-

from odoo import fields, models


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "estate property offer"

    price = fields.Float('Price')
    status = fields.Char()

    partner_id = fields.Many2one("res.partner", string="Partner")
    property_id = fields.Many2one('estate.property', string='Property')
    validity = fields.Integer(
        'Validity (days)', default=7, inverse="_inverse_validity")
    date_deadline = fields.Datetime('Deadline', inverse="_inverse_date_deadline")

    def _inverse_validity(self):
        for record in self:
            if not record.date_deadline and record.create_date:
                record.date_deadline = fields.Datetime.add(
                    record.create_date, days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            if record.date_deadline:
                record.validity = (record.date_deadline -
                                   record.create_date).days
