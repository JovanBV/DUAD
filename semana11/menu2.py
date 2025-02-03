import actions2
import data2

''' Validates that the user enters a numeric menu option. '''
def validate_menu_option(option):
    while True:
        try: 
            return int(option)
        except ValueError:
            option = input('Type a valid option from the menu: ')


''' Executes the function corresponding to the selected menu option. '''
def menu_options(option, students_list, student_headers, path):
    match option:  
        case 1: actions2.Student.create_student(students_list)
        case 2: actions2.show_all_data(students_list)
        case 3: actions2.find_top_3_average(students_list)
        case 4: actions2.calculate_avg_avg(students_list)
        case 5: data2.export_csv_file(path, students_list, student_headers)
        case 6: data2.import_csv_file(path, students_list)
