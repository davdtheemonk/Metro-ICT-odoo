from odoo import models, fields

class Exam(models.Model):
    _name = "exams_ranking_system.exam"
    name = fields.Char(string="Name", required=True)
    date = fields.Date(string="Date", required=True)
    total_marks = fields.Float(string="Total Marks", required=True)
    result_ids = fields.One2many('exams_ranking_system.examresult', 'exam_id', string="Results")
