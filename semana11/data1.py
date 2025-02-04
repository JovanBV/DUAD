import csv
import main1

''' 
Exports student data to a CSV file. 
Converts instances to dictionaries before exporting.
'''
def export_csv_file(path, students_list, student_headers):
    '''
    This function exports the student data to a CSV file. The data from each student 
    is first converted into a dictionary and then written to the CSV file.
    '''
    new_data = []
    for student in students_list:
        new_data.append(instance_to_dict(student))
    with open(path, 'w') as file:
        writer = csv.DictWriter(file, student_headers)
        writer.writeheader()
        writer.writerows(new_data)


''' 
Imports student data from a CSV file and appends it to the list.
'''
def import_csv_file(path, students_list):
    '''
    This function imports student data from a CSV file and appends the data to the 
    list of students. It creates Student instances for each row in the CSV file.
    '''
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        if not rows:
            print("\nNo information to import.\n")
        for row in reader:
            imported_student = main1.Student(row)
            students_list.append(imported_student)


''' 
Converts an instance entry to a dictionary.
'''
def instance_to_dict(student):
    '''
    This function converts a Student instance to a dictionary by using the __dict__ method.
    '''
    new_value = student.__dict__
    return new_value
