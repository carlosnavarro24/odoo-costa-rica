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

import netsvc
from osv import fields, osv
import tools
from tools.translate import _

class hr_contract(osv.osv):
    """
    Employee contract based on the visa, work permits
    allows to configure different Salary structure
    """

    _inherit = 'hr.contract'
    _description = 'Employee Contract'
    _columns = {
        'schedule_pay': fields.selection([
            ('fortnightly', 'Fortnightly'),
            ('monthly', 'Monthly'),
            ('quarterly', 'Quarterly'),
            ('semi-annually', 'Semi-annually'),
            ('annually', 'Annually'),
            ('weekly', 'Weekly'),
            ('bi-weekly', 'Bi-weekly'),
            ('bi-monthly', 'Bi-monthly'),
            ], 'Scheduled Pay', select=True),
    }

    _defaults = {
        'schedule_pay': 'monthly',
    }
    
hr_contract()

class hr_job(osv.osv):
    _inherit = 'hr.job'
    _columns = {
        'code': fields.char('Code', size=128, required=False),
    }

hr_job()


class hr_payslip_run(osv.osv):
    _inherit = 'hr.payslip.run'
    _columns = {
        'schedule_pay': fields.selection([
            ('fortnightly', 'Fortnightly'),
            ('monthly', 'Monthly'),
            ('quarterly', 'Quarterly'),
            ('semi-annually', 'Semi-annually'),
            ('annually', 'Annually'),
            ('weekly', 'Weekly'),
            ('bi-weekly', 'Bi-weekly'),
            ('bi-monthly', 'Bi-monthly'),
            ], 'Scheduled Pay', select=True, readonly=True, states={'draft': [('readonly', False)]}),
    }

    def confirm_payslips(self, cr, uid, ids, context=None):
        for payslip_run in self.browse(cr, uid, ids, context=context):
            payslip_obj = self.pool.get('hr.payslip')
            payslips = payslip_obj.browse(cr, uid, payslip_run.slip_ids, context)
            for payslip in payslips:
                payslip_id = payslip.id
                payslip_id.process_sheet()

hr_payslip_run()

class HrPayslip(osv.osv):
    _inherit = 'hr.payslip'

    _columns = {
                'name': fields.char('Description', size=256, required=False, readonly=True, states={'draft': [('readonly', False)]}),
    }

    def onchange_employee_id(self, cr, uid, ids, date_from, date_to, employee_id=False, contract_id=False, context=None):
        res = super(HrPayslip, self).onchange_employee_id(cr, uid, ids, date_from, date_to, employee_id=employee_id, contract_id=contract_id, context=context)
        
        if (not employee_id) or (not date_from) or (not date_to):
            return res
        
        employee_obj = self.pool.get('hr.employee')
        contract_obj = self.pool.get('hr.contract')
        
        employee = employee_obj.browse(cr, uid, employee_id, context=context)
        
        if (not contract_id):
            contract_id = contract_obj.search(cr, uid, [('employee_id', '=', employee_id)], context=context)
        else:
            contract_id = [contract_id]
        
        contract = contract_obj.browse(cr, uid, contract_id, context=context)[0]
        schedule_pay = ''
        if contract.schedule_pay:
            #This is to translate the terms 
            if contract.schedule_pay == 'weekly':
                schedule_pay = _('weekly')
            elif contract.schedule_pay == 'monthly':
                schedule_pay = _('monthly')

        name = _('%s payroll of %s from %s to %s') % (schedule_pay, employee.name, date_from, date_to)
        name = name.upper()
        worked_days_line_list = []
        if res['value']['worked_days_line_ids']:
            worked_days_line = res['value']['worked_days_line_ids'][0]
            worked_days_line['code'] = 'HN'
            worked_days_line['name'] = name
            worked_days_line_list = [worked_days_line]
        
        res['value'].update({
                    'name': name,
                    'worked_days_line_ids' : worked_days_line_list,
        })

        return res

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
