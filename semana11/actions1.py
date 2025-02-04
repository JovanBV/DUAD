import heapq

''' Requests student information and returns a dictionary with the data. 
    Ensures grades are numeric and within the valid range. '''
def type_student_info(student_headers):
    new_student = dict.fromkeys(student_headers)
    for key in student_headers:
        if key in student_headers[:2]:  # Full name & Class section
            new_data = input(f'\nType the {key}: ')
        elif key in student_headers[2:6]:  # Grades
            new_data = validate_grades(input(f'\nType the {key}: '))
        elif key == student_headers[6]:  # Grades average
            student_grades = [new_student['Spanish grade'], new_student['English grade'], 
                new_student['Social studies grade'], new_student['Science grade']]
            new_data = sum(student_grades) / 4
        new_student[key] = new_data
    return new_student


class Student:
    student_subjects = ['Full name', 'Class section', 'Spanish grade', 'English grade', 'Social studies grade', 'Science grade']

    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        for grades in self.student_subjects: 
            self.grades[subject] = grade


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