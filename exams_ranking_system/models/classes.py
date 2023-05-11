from odoo import models, fields

class Classes(models.Model):
    _name = "exams_ranking_system.classes"
    name = fields.Char(string="Name", required=True)
    student_ids = fields.One2many('exams_ranking_system.student', 'class_id', string="Students")
    school_id = fields.Many2one('exams_ranking_system.school',required=True)