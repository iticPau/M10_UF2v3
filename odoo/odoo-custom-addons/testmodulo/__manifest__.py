# -*- coding: utf-8 -*-
{
    'name': 'Test Modulo',
    'version': '1.0',
    'summary': 'Gestiona eventos, horarios de limpieza y salidas turísticas',
    'description': 'Este módulo permite gestionar eventos, horarios de limpieza y salidas turísticas.',
    'category': 'Uncategorized',
    'author': 'Your Name',
    'website': 'http://www.yourwebsite.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/testmodulo_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
