# -*- coding: utf-8 -*-

from odoo import models, fields, api


class marketing(models.Model):
    _name = 'marketing.test'
    _description = 'Esto es un test hehe'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
