# -*- coding: utf-8 -*-

from odoo import fields, models
from odoo.exceptions import UserError

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
    
    def accept(self):
        for record in self:
            property_id = self.property_id 
            if property_id.has_active_offer():
                raise UserError("You can't accept an offer while there is an active offer")
            if property_id:
                property_id.set_selling_price(record.price)
                if record.partner_id: property_id.set_buyer(record.partner_id) 
            record.status = 'Accepted'


    def refuse(self):
        for record in self:
            record.status = 'Refused'