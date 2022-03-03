# -*- coding: utf-8 -*-
# Copyright 2016, 2020 Openworx - Mario Gielissen
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Agrista Backend Theme",
    "summary": "Inspired by Openworx Material Backend Theme V14",
    "version": "14.0.0.2",
    "category": "Theme/Backend",
    "website": "https://www.openworx.nl",
    "description": """
		Inspired by Openworx Material Backend theme for Odoo 14.0 community edition.
    """,
    'images': [
        'images/screen.png'
    ],
    "author": "Agrista",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        'web',
        'web_responsive',

    ],
    "data": [
        'views/assets.xml',
        # 'views/res_company_view.xml',
        'views/users.xml',
        'views/sidebar.xml',
    ],
    # 'live_test_url': 'https://youtu.be/JX-ntw2ORl8'

}
