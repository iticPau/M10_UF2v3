from odoo import models, fields

class CleaningSchedule(models.Model):
    _name = 'testmodulo.cleaning_schedule'
    _description = 'Empleados de limpieza'

    name = fields.Char(string='Nombre de limpiador', required=True)
    start_datetime = fields.Datetime(string='Inicio de limpieza', required=True)
    end_datetime = fields.Datetime(string='Fin de limpieza', required=True)
    description = fields.Text(string='Descripción')


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
        ('diamante', 'Diamante')
    ], string='Tipo del cliente', required=True)


class TouristicOuting(models.Model):
    _name = 'testmodulo.touristic_outing'
    _description = 'Salidas turísticas'

    name = fields.Char(string='Nombre de la ruta', required=True)
    start_datetime = fields.Datetime(string='Fecha y hora de inicio', required=True)
    end_datetime = fields.Datetime(string='Fecha y hora de finalización', required=True)
    description = fields.Text(string='Descripción')
