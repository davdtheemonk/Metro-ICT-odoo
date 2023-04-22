from odoo import models, fields

class Ranking(models.Model):
    _name="exams_ranking_system.ranking"
    exam = fields.Many2one('exams_ranking_system.exam', string="Exams")