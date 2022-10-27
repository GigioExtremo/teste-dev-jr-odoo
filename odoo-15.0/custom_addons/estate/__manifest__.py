{
    'name': 'Real Estate',
    'version': '15.0.0.1.0.0',
    'author': 'Giovanni Dilly',
    'category': 'Uncategorized',
    'summary': 'Real Estate module',
    'description': """
        A beginner's module from Odoo tutorial.
    """,
    'depends': [],
    'data': [
        'security\\ir.model.access.csv',
        'views\\estate_settings_views.xml',
        'views\\estate_advertisements_views.xml',
        'views\\estate_offers_views.xml',
        'views\\estate_menus.xml'
    ],
    'installable': True,
    'auto_install': False,
    "application": True,
    'license': 'LGPL-3',
}
