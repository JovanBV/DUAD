import heapq
import csv

def main():
    students_list = []
    path = 'C:/Users/jovan/Documents/DUAD/semana11/students_information.txt'
    student_headers = ['Full name', 'Class section', 'Spanish grade', 'English grade', 
    'Social studies grade', 'Science grade', 'Grades average']

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
        option = validate_menu_option(option)
        menu_options(option, students_list, student_headers, path)


def validate_menu_option(option):
    while True:
        try: 
            return int(option)
        except ValueError:
            option = input('Type a valid option from the menu: ')


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
    def __init__(self, dictionary_student):
        self.name = dictionary_student['Full name']
        self.class_section = dictionary_student['Class section']
        self.spanish_grade = dictionary_student['Spanish grade']
        self.english_grade = dictionary_student['English grade']
        self.social_studies_grade = dictionary_student['Social studies grade']
        self.grades_average = dictionary_student['Grades average']

def menu_options(option, students_list, student_headers, path):
    match option:  
        case 1: 
            student = Student(type_student_info(student_headers))
            students_list.append(student)
        case 2: show_all_data(students_list)
        case 3: find_top_3_average(students_list)
        case 4: calculate_avg_avg(students_list)
        case 5: export_csv_file(path, students_list, student_headers)
        case 6: import_csv_file(path, students_list)


''' Displays all students' information. '''
def show_all_data(students_list):
    for student in students_list:
        print(f'{student.name}: {student.class_section}, {student.spanish_grade}, {student.english_grade}, {student.social_studies_grade}, {student.grades_average}')


''' Finds and displays the top 3 students with the highest average grades. '''
def find_top_3_average(students_list):
    students_avg = [float(student.grades_average) for student in students_list]
    students_name = [student.name for student in students_list]

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
    students_avg = [float(student.grades_average) for student in students_list]
    average = sum(students_avg) / len(students_avg)
    print(f'\nOverall average grade: {average:.2f}\n')



def export_csv_file(path, students_list, student_headers):
    with open(path, 'w') as file:
        writer = csv.DictWriter(file, student_headers)
        writer.writeheader()
        writer.writerows(students_list)


''' Imports student data from a CSV file and appends it to the list. '''
def import_csv_file(path, students_list):
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        if not rows:
            print("\nThere's no information to import\n")
        for data in rows:
            students_list.append(data)
            













main()
