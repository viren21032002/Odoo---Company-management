from odoo import fields, api, models, _


class EmployeeData(models.Model):
    _name = 'employee.data'
    _description = 'Employee data'
    _rec_name = 'name'
    name = fields.Char(string="Employee's name")
    employee_id = fields.Char(string="Employee's ID")
    employee_age = fields.Integer(string="Age")
    employee_phone_number = fields.Integer(string="Phone no.")
    company_name = fields.Char(string="Company", default="Aktiv software", readonly=True)
    employee_position_id = fields.Many2one('designation.data', string="Employee's designation")
    employee_department_id = fields.Many2one('department.data', string="Choose department")
    employee_experience = fields.Integer(string="Experience in years")
    # project_ids = fields.Many2many('project.details', 'project_id', string="Assigned projects")

    @api.model
    def create(self, vals):
        if not vals['employee_id']:
            find_emp_id = self.env['ir.sequence'].next_by_code('employee.id')

            vals['employee_id'] = find_emp_id

            return super(EmployeeData, self).create(vals)





