# -*- coding: utf-8 -*-
# This file is part of Odoo. The COPYRIGHT file at the top level of
# this module contains the full copyright notices and license terms.

{
    'name': 'Partner Debitoren- / Kreditorenkonto',
    'version': '13.0.1.0.8',
    'author': 'syscoon GmbH',
    'license': 'OPL-1',
    'category': 'Accounting',
    'website': 'https://syscoon.com',
    'depends': [
        'base',
        'account'
    ],
    'description': """If a partner is created a new debit and credit account will be created following a 
    sequence that can be created individually per company.""",
    'init_xml': [],
    'demo_xml': [],
    'data': [
        'data/partner_account_company_data.xml',
        'views/res_config_settings_views.xml',
        'views/res_partner.xml',
        'security/ir.model.access.csv',
        ],
    'active': False,
    'installable': True
}
