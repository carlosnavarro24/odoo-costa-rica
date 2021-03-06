# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Addons modules by CLEARCORP S.A.
#    Copyright (C) 2009-TODAY CLEARCORP S.A. (<http://clearcorp.co.cr>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Webkit based extended report financial report',
    'description': "",
    'version': '1.0',
    'author': 'CLEARCORP S.A.',
    'category': 'Finance',
    'website': "http://clearcorp.co.cr",
    'images': [],
    'depends': ['account' ],
    'init_xml': [],
    'demo_xml' : [],
    'update_xml': ['account_move_line_view.xml',
                   'data/financial_webkit_header.xml',
                   'report/report.xml',
                   'wizard/account_bank_balances_wizard_view.xml',
                   'wizard/l10n_cr_partners_ledger_wizard_view.xml',
                   'wizard/l10n_cr_open_invoices_wizard_view.xml',
                   'report_menus.xml',
                   'account_view.xml',
                   ],
    'test': [],
    'active': False,
    'installable': True,
    'license': 'AGPL-3',
}
