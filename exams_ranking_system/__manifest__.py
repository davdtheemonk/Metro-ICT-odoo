{
    "name":"Exams Ranking System"
    ,
    'version': '1.0',
    'summary': 'An exam ranking system',
    'sequence': 1,
    'description': """
    Long Description of your modules""",
    'author': 'David mugalla',
    'company': 'Metro ICT',
    'website': '',
    'depends': ['base'],
    'data': [
        'views/menu.xml',
        'views/exam_views.xml',
        'views/examresults.xml',
        'views/ranking.xml',
        'views/student_views.xml',
        'security/ir.model.access.csv',
         'views/assets.xml',
       
        
   ],
     'js': [
        'static/js/ranking.js',
    ],
     
    'application': True,
}