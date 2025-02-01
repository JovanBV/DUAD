import csv

''' Exports student data to a CSV file. '''
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
            