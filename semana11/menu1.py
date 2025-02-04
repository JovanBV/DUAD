import actions1
import data1
import main1


def validate_menu_option(option):
    while True:
        try: 
            return int(option)
        except ValueError:
            option = input('Please enter a valid option from the menu: ')


def menu_options(option, students_list, student_headers, path):
    '''
    This function handles the different menu options and calls the corresponding
    functions to perform the required operations.
    '''
    match option:  
        case 1: 
            student = main1.Student(data1.type_student_info(student_headers))
            students_list.append(student)
            print(student.name)
            data1.instance_to_dict(student)
        case 2: actions1.show_all_data(students_list)
        case 3: actions1.find_top_3_average(students_list)
        case 4: actions1.calculate_avg_avg(students_list)
        case 5: data1.export_csv_file(path, students_list, student_headers)
        case 6: data1.import_csv_file(path, students_list)

