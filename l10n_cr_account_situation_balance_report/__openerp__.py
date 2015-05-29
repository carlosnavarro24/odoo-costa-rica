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
    'name': 'Situation Balance Report',
    'version': '1.0',
    'author': 'Clearcorp',
    'category': 'Finance',
    'description': """
Situation Balance Report:
===========================
Create the situation balance report
    """,    
    'website': "http://clearcorp.co.cr",
    'depends': ['account_report_lib', ],
    'data': [
             'data/report_paperformat.xml',
             'security/ir.model.access.csv',
             'report/report.xml',
             'wizard/l10n_cr_account_situation_balance_wizard_view.xml',
             'report_menus.xml',
             'views/report_situation_balance.xml',
            ],
    'active': False,
    'installable': True,
    'license': 'AGPL-3',
}

