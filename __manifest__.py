# -*- coding: utf-8 -*-
{
    'name': "Location de véhicules",

    'summary': "Gestion d'une location de véhicules",

    'description': """Ce module permet de gérer la location de véhicules""",

    'author': "Mapluz",
    'website': "https://www.mapluz.fr",

    'category': 'inventory/cars',
    'version': '18.0.1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'assets': {
            'web.assets_backend': ['rentcars/static/src/css/group_border.css',],
            'web.assets_frontend':['rentcars/static/src/css/group_border.css',],
              },
    'application': True,
    'license': "LGPL-3",
    'images': [
        'static/img/cover_image.png',
    ],
    # always loaded
    'data': [
        'security/rentcars_security.xml',
        'security/ir.model.access.csv',
        'views/rentcars_menu.xml',
        'views/vehicle_views.xml',
        'views/vehicle_list_template.xml',
        'views/vehicle_detail_template.xml',
        'views/garage_views.xml',
        'views/option_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/garage.xml',
        'demo/options.xml',
        'demo/vehicle.xml',
    ],
}

