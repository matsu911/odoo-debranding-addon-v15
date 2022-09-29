# -*- coding: utf-8 -*-
{
    'name': "Odoo Debranding for v15",

    'summary': """
        Odoo Module for backend and frontend debranding.""",

    'description': """
        To debrand front-end and back-end pages by removing
         odoo promotions, links, labels and other related
         stuffs.
    """,

    'author': "matsu911",
    'website': "https://github.com/matsu911/odoo-debranding-addon-v15",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base_setup',
        'web',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'odoo-debranding-addon-v15/static/src/js/UserMenu.js',
        ],
    },
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'license': "AGPL-3",
    'installable': True,
    'application': True,
}
