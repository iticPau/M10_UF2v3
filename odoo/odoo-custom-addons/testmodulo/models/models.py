from odoo import models, fields, api

class CleaningSchedule(models.Model):
    _name = 'testmodulo.cleaning_schedule'
    _description = 'Empleados de limpieza'

    name = fields.Char(string='Nombre de limpiador', required=True)
    start_datetime = fields.Datetime(string='Inicio de limpieza', required=True)
    end_datetime = fields.Datetime(string='Fin de limpieza', required=True)
    description = fields.Text(string='Descripción')
    cleaning_area = fields.Selection([
        ('A1-A10', 'A1-A10'),
        ('B1-B10', 'B1-B10'),
        ('C1-C10', 'C1-C10'),
        ('D1-D10', 'D1-D10'),
        ('E1-E10', 'E1-E10')
    ], string='Áreas de limpieza', required=True)
class Event(models.Model):
    _name = 'testmodulo.event'
    _description = 'Eventos'

    name = fields.Char(string='Nombre del evento', required=True)
    start_datetime = fields.Datetime(string='Inicio del evento', required=True)
    end_datetime = fields.Datetime(string='Fin del evento', required=True)
    description = fields.Text(string='Descripción')
    customer_type = fields.Selection([
        ('bronce', 'Bronce'),
        ('oro', 'Oro'),
        ('diamante', 'Diamante'),
        ('todos','Todos')
    ], string='Tipo del cliente', required=True)
    color = fields.Integer(string="Color")
    event_count = fields.Integer(string="Cantidad de eventos", compute='_compute_event_count')
    
    @api.depends('customer_type')
    def _compute_event_count(self):
        for record in self:
            record.event_count = self.env['testmodulo.event'].search_count([('customer_type', '=', record.customer_type)])
    
    @api.model
    def count_events_by_customer_type(self):
        counts = self.read_group([('customer_type', '!=', False)], ['customer_type'], ['customer_type'])
        return {group['customer_type']: group['customer_type_count'] for group in counts}


    @api.depends('customer_type')
    def _compute_color(self):
        for record in self:
            if record.customer_type == 'bronce':
                record.color = 1  # Rojo
            elif record.customer_type == 'oro':
                record.color = 2  # Amarillo
            elif record.customer_type == 'diamante':
                record.color = 3  # Azul
            else:
                record.color = 0  
    

class TouristicOuting(models.Model):
    _name = 'testmodulo.touristic_outing'
    _description = 'Salidas turísticas'

    name = fields.Char(string='Nombre de la ruta', required=True)
    start_datetime = fields.Datetime(string='Fecha y hora de inicio', required=True)
    end_datetime = fields.Datetime(string='Fecha y hora de finalización', required=True)
    description = fields.Text(string='Descripción')
