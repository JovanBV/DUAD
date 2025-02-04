import heapq

''' 
Requests student information and returns a dictionary with the data. 
It ensures that grades are numeric and within the valid range.
'''
def type_student_info(student_headers):
    new_student = dict.fromkeys(student_headers)
    for key in student_headers:
        if key in student_headers[:2]:  # Full name & Class section
            new_data = input(f'\nEnter the {key}: ')
        elif key in student_headers[2:6]:  # Grades
            new_data = validate_grades(input(f'\nEnter the {key}: '))
        elif key == student_headers[6]:  # Grades average
            student_grades = [new_student['spanish_grade'], new_student['english_grade'], 
                new_student['social_studies_grade'], new_student['science_grade']]
            new_data = sum(student_grades) / 4
        new_student[key] = new_data
    return new_student


''' 
Displays all students' information.
'''
def show_all_data(students_list):
    '''
    This function iterates over the list of students and prints their details 
    including name, class section, grades, and average grade.
    '''
    for student in students_list:
        print(f'{student.name}: {student.class_section}, {student.spanish_grade}, {student.english_grade}, {student.social_studies_grade}, {student.grades_average}')


''' 
Finds and displays the top 3 students with the highest average grades.
'''
def find_top_3_average(students_list):
    '''
    This function calculates and displays the top 3 students with the highest 
    average grades.
    '''
    students_avg = [float(student.grades_average) for student in students_list]
    students_name = [student.name for student in students_list]

    top_3 = heapq.nlargest(3, zip(students_avg, students_name))
    print('\nTop 3 students with highest averages:\n')
    for avg, name in top_3:
        print(f'- {name}: {avg}\n')


''' 
Ensures that the entered grade is a number between 0 and 100.
'''
def validate_grades(grade):
    '''
    This function validates that the entered grade is numeric and between 0 and 100. 
    If the input is invalid, it prompts the user to enter a valid grade.
    '''
    while True:
        try:
            grade = float(grade)
            if 0 <= grade <= 100:
                return grade
            else:
                grade = input('Please enter a grade between 0 and 100: ')
        except ValueError:
            grade = input('Please enter a valid grade: ')


''' 
Calculates and displays the overall average grade of all students.
'''
def calculate_avg_avg(students_list):
    '''
    This function calculates and displays the overall average grade of all students 
    by averaging the grades of all students in the list.
    '''
    students_avg = [float(student.grades_average) for student in students_list]
    average = sum(students_avg) / len(students_avg)
    print(f'\nOverall average grade: {average:.2f}\n')
