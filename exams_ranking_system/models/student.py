from odoo import models, fields

class Student(models.Model):
    _name="exams_ranking_system.student"
    first_name = fields.Char(string="First Name",required=True)
    last_name = fields.Char(string='Last Name', required=True)
    email = fields.Char(string="Email", required=True)
    result_ids = fields.One2many('exams_ranking_system.examresult', 'student_id', string="Results")
