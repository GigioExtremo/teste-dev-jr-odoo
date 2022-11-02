{
    'name': 'Real Estate Account',
    'version': '15.0.0.1.0.0',
    'author': 'Giovanni Dilly',
    'category': 'Uncategorized',
    'summary': 'Real Estate module',
    'description': """
        A complementary module to "estate", as described by the Odoo tutorial.
    """,
    'depends': ['estate', 'account'],
    'data': [
        # 'security\\ir.model.access.csv',
        # 'views\\res_user_property_view.xml'
    ],
    'installable': True,
    'auto_install': False,
    "application": True,
    'license': 'LGPL-3',
}
