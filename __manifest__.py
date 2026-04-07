# -*- coding: utf-8 -*-
{
    'name': "Google Indexing for Website Pages",

    'summary': "Automatically notifies Google Indexing API when website pages are created, updated or deleted",

    'description':  """
Google Indexing for Odoo Website Pages
======================================

This module integrates the Google Indexing API with your Odoo website.

✨ Features:
Automatically notifies Google when a website page is created, updated, or deleted.
Helps get your new or updated pages indexed by Google faster.
Stores service account JSON key path securely in system parameters.
Easy configuration from Odoo Settings.

⚙ Technical:
Hooks into website.page model (create, write, unlink).
Calls Google Indexing API using the official Python client.
Logs responses and errors for transparency.

Ideal for SEO optimization on Odoo-based websites.

""",

    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Others',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/res_config_settings_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
