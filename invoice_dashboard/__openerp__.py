# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright :
#        (c) 2016 Jonathan Bravo, (Guayaquil, Ecuador, http://www.jonathanbravo.com)
#                 Jonathan Bravo <jjbravo88@gmail.com.com>
#
##############################################################################

{
    'name' : 'Odoo Invoice Dashboard V9',
    'description': """

Este modulo permite mostrar graficos semanales como en al version 9 de odoo.
--
This module allows you to display weekly charts as in the version 9 of Odoo.

	""",
    'version': '8.0.1.0.0',
    'category': 'Accounting',
    'author' : 'Jonathan Bravo @jbravot',
    'complexity': 'normal',
    'website': 'http://jbravot.github.io/portafolio/',
    'data': [
        'views/account_journal_dashboard_view.xml'
    ],
    'depends' : [
        'account',
        'web_kanban_graph',
    ],
    'js': [],
    'css': [],
    'qweb': [],
    "images": [
		"static/description/example.jpg",
	],
    'installable': True,
    'auto_install': False,
}
