# -*- coding: utf-8 -*-

from odoo import fields, models


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "estate property offer"

    price = fields.Float('Price')
    status = fields.Char(readonly=True)

    partner_id = fields.Many2one("res.partner", string="Partner")
    property_id = fields.Many2one('estate.property', string='Property')
