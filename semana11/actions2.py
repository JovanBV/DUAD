import heapq

class Student:
    def __init__(self, name, class_section, spanish_grade, english_grade, social_studies_grade, science_grade):
        self.name = name
        self.class_section = class_section
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.social_studies_grade = social_studies_grade
        self.science_grade = science_grade

    def create_student(students_list):
        name = input('Type the name of the student: ')
        class_section = input('Type the class were the student belonges: ')
        spanish_grade = validate_grades(input('Type the students spanish grade: '))
        english_grade = validate_grades(input('Type the students english grade: '))
        social_studies_grade = validate_grades(input('Type the students social studies grade: '))
        science_grade = validate_grades(input('Type the students sciencie grade: '))
        students_list.append(Student(name, class_section, spanish_grade, english_grade, social_studies_grade, science_grade))


''' Displays all students' information. '''
def show_all_data(students_list):
    for student in students_list:
        print(f"\n{student['Full name']}, {student['Class section']}, {student['Spanish grade']}, "
            f"{student['English grade']}, {student['Social studies grade']}, {student['Science grade']}, "
            f"{student['Grades average']}")


''' Finds and displays the top 3 students with the highest average grades. '''
def find_top_3_average(students_list):
    students_avg = [float(student['Grades average']) for student in students_list]
    students_name = [student['Full name'] for student in students_list]

    top_3 = heapq.nlargest(3, zip(students_avg, students_name))
    print('\nTop 3 students with highest averages:\n')
    for avg, name in top_3:
        print(f'- {name}: {avg}\n')


''' Ensures the entered grade is a number between 0 and 100. '''
def validate_grades(grade):
    while True:
        try:
            grade = float(grade)
            if 0 <= grade <= 100:
                return grade
            else:
                grade = input('Type a grade between 0 and 100: ')
        except ValueError:
            grade = input('Type a valid grade: ')


''' Calculates and displays the overall average grade of all students. '''
def calculate_avg_avg(students_list):
    students_avg = [float(student['Grades average']) for student in students_list]
    average = sum(students_avg) / len(students_avg)
    print(f'\nOverall average grade: {average:.2f}\n')