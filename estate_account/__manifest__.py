# -*- coding: utf-8 -*-
{
    'name': "Estate_Account",
    'summary': """""",
    'description': """Long description of module's purpose""",
    'author': "Awadhesh Giri ,  iTech Classes",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'price': '2.0',
    'currency': 'USD',
    'version': '0.1',

    'depends': ['real_estate', 'account'],
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
    'license': 'LGPL-3',
}
