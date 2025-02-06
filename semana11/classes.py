class Student:
    '''
    This class represents a student and stores their information such as name, 
    class section, grades, and average grade.
    '''
    def __init__(self, dictionary_student):
        self.name = dictionary_student['name']
        self.class_section = dictionary_student['class_section']
        self.spanish_grade = dictionary_student['spanish_grade']
        self.english_grade = dictionary_student['english_grade']
        self.social_studies_grade = dictionary_student['social_studies_grade']
        self.science_grade = dictionary_student['science_grade']
        self.grades_average = dictionary_student['grades_average']

