import menu1

def main():
    students_list = []
    path = 'C:/Users/jovan/Documents/DUAD/semana8/students_information.txt'
    student_headers = ['name', 'class_section', 'spanish_grade', 'english_grade', 
    'social_studies_grade', 'science_grade', 'grades_average']

    option = 0
    while option != 7: 
        option = input(
            '-----------------------------------------\n'
            '1) Register a new student\n'
            '2) See all students\' information\n'
            '3) See the top 3 students with the highest average grade\n'
            '4) See the average grade of all students\n'
            '5) Export data to CSV\n'
            '6) Import data from CSV\n'
            '7) Exit\n'
            'Type your option: '
        )
        option = menu1.validate_menu_option(option)
        menu1.menu_options(option, students_list, student_headers, path)

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








main()
