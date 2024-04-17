from odoo import fields, api, models, _


class DepartmentData(models.Model):
    _name = 'department.data'
    _description = 'Department'
    _rec_name = 'name'
    name = fields.Char(string='Department name')

