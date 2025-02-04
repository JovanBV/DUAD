import actions
import data

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
        case 1: students_list.append(actions.type_student_info(student_headers))
        case 2: actions.show_all_data(students_list)
        case 3: actions.find_top_3_average(students_list)
        case 4: actions.calculate_avg_avg(students_list)
        case 5: data.export_csv_file(path, students_list, student_headers)
        case 6: data.import_csv_file(path, students_list)
