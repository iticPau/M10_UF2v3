# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class Controllers(http.Controller):

    @http.route('/testmodulo/events', type='json', auth='user')
    def get_events(self, start_datetime, end_datetime):
        events = request.env['testmodulo.event'].search([
            ('start_datetime', '>=', start_datetime),
            ('end_datetime', '<=', end_datetime)
        ])
        return events.read(['name', 'start_datetime', 'end_datetime', 'description', 'customer_type'])

    @http.route('/testmodulo/cleaning_schedule', type='json', auth='user')
    def get_cleaning_schedule(self, start_datetime, end_datetime):
        cleaning_schedule = request.env['testmodulo.cleaning_schedule'].search([
            ('start_datetime', '>=', start_datetime),
            ('end_datetime', '<=', end_datetime)
        ])
        return cleaning_schedule.read(['name', 'start_datetime', 'end_datetime', 'description'])

    @http.route('/testmodulo/touristic_outings', type='json', auth='user')
    def get_touristic_outings(self, start_datetime, end_datetime):
        touristic_outings = request.env['testmodulo.touristic_outing'].search([
            ('start_datetime', '>=', start_datetime),
            ('end_datetime', '<=', end_datetime)
        ])
        return touristic_outings.read(['name', 'start_datetime', 'end_datetime', 'description'])
