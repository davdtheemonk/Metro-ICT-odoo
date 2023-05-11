from odoo import models, fields

class School(models.Model):
    _name = "exams_ranking_system.school"
    name = fields.Char(string="Name", required=True)
    class_id = fields.One2many('exams_ranking_system.classes', 'school_id',string="Classes")
