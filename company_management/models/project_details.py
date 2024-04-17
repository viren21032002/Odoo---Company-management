from odoo import fields, api, models, _


class ProjectDetails(models.Model):
    _name = 'project.details'
    _description = "Project details"
    _rec_name = "name"
    name = fields.Char(string="Project name")
    project_department_id = fields.Many2one('department.data', string="Department")
    project_team_lead_ids = fields.Many2many('employee.data', 'project_team_lead_id', string="Team leads")
    project_manager_id = fields.Many2one('employee.data', string="Project manager")
    emp_data_ids = fields.One2many('employee.register', 'project_details_relation_id', string="Assign Employee")
