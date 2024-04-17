from odoo import fields, api, models, _


class DesignationData(models.Model):

    _name = 'designation.data'
    _description = 'Designation data'
    _rec_name = 'name'

    name = fields.Char(string='Designation')
