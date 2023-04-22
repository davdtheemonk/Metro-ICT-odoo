from odoo import models, fields

class ExamResult(models.Model):
    _name='exams_ranking_system.examresult'
    student_id = fields.Many2one('exams_ranking_system.student',required=True)
    exam_id = fields.Many2one('exams_ranking_system.exam', string='Exam')
    marks_obtained = fields.Float(string="Marks Obtained", required=True)
    ranking = fields.Integer(string="ranking", required=True)
    def calculate_ranking(self):
        """Calculate the ranking for the associated exam."""
        # Get the associated exam
        exam = self.exam_id
        # Get all the exam results for the associated exam
        exam_results = self.env['exams_ranking_system.examresult'].search([('exam_id', '=', exam.id)])
        # Sort the exam results by marks obtained in descending order
        sorted_exam_results = exam_results.sorted(key=lambda r: r.marks_obtained, reverse=True)# Update the ranking for each exam result
        rank = 1
        for result in sorted_exam_results:
            result.write({'ranking': rank})
            rank += 1
