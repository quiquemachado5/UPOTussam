# -*- coding: utf-8 -*-
{
    'name': "UPOTUSSAM",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml'
        'views/view-pasajero.xml',
        'views/view-boletos.xml',
        'views/view-conductor.xml',
        'views/view-autobus.xml',
        'views/view-autobus-linea.xml',
        'views/view-lineas.xml',
        'views/view-paradaPorLinea.xml',
        'views/view-paradas.xml',
        'views/view-descuento.xml',
        'views/view-nomina.xml',
        'views/templates.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}