# -*- coding: utf-8 -*-

{
    'name': 'Co-op Volunteering',
    'summary': """App to manage Co-op Volunteers and Volunteering""",
    'description': """
        App to manage Co-op Volunteers and Volunteering:
        -Volunteers
        -Volunteer hours
        -Co-op storefront
    """,
    
    'author': 'Sheraya Smith',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [
        'security/coop_security.xml',
        'security/ir.model.access.csv',
        'views/coop_menuitems.xml',
        'views/coop_views.xml',        
    ], 
    
    'demo': [
        'demo/coop_demo.xml',        
    ],
}