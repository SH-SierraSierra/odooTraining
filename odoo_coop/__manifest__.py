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
        'views/coop_views.xml',        
    ], 
    
    'demo': [
        'demo/coop_demo.xml',        
    ],
}