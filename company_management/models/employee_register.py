from odoo import fields, api, models, _


class EmployeeRegister(models.Model):
    _name = 'employee.register'
    _description = 'Employee register'
    employee_id = fields.Many2one('employee.data', string='Department name')
    designation_id = fields.Many2one('designation.data', string="Position")
    project_details_relation_id = fields.Many2one('project.details')

    @api.onchange('employee_id')
    def _onchange_employee_id(self):
        for rec in self:
            if rec.employee_id:
                designation_search = self.env['employee.data'].search([('id', '=', rec.employee_id.id)])
                rec.designation_id = designation_search.employee_position_id.id
