# -*- coding: utf-8 -*-
{
    'name': "Real Estate - Invoice ",
    'summary': """""",
    'description': """Some Extra Feature for Real Estate Module Like Invoicing and Playground(Compiler)""",
    'author': "Awadhesh Giri ,  iTech Classes",
    'website': "http://www.demonstrate.com",
    'category': 'Real Estate Property ',
    'price': '2.0',
    'currency': 'USD',
    'license': 'OPL-1',
    'version': '15.0.1.1.0',

    'depends': ['real_estate_apps', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/odoo_playground_view.xml',
        'views/templates.xml',
    ],
    'demo': [
        'views/templates.xml',
    ],
    'installable': True,
    'application': True,
    'auto-install': False,
    
}
