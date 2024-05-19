# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.http import route

class controllers(http.Controller):

    @http.route('/testmodulo/events', type='json', auth='user')
    def get_events(self, start_date, end_date):
        events = request.env['testmodulo.event'].search([
            ('start_date', '>=', start_date),
            ('end_date', '<=', end_date)
        ])
        return events.read(['name', 'start_date', 'end_date', 'description'])

    @http.route('/testmodulo/cleaning_schedule', type='json', auth='user')
    def get_cleaning_schedule(self, start_date, end_date):
        cleaning_schedule = request.env['testmodulo.cleaning_schedule'].search([
            ('date', '>=', start_date),
            ('date', '<=', end_date)
        ])
        return cleaning_schedule.read(['name', 'date', 'description'])

    @http.route('/testmodulo/touristic_outings', type='json', auth='user')
    def get_touristic_outings(self, start_date, end_date):
        touristic_outings = request.env['testmodulo.touristic_outing'].search([
            ('date', '>=', start_date),
            ('date', '<=', end_date)
        ])
        return touristic_outings.read(['name', 'date', 'description'])