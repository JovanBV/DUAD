def read_file(path, list):
    with open(path) as file:
        for line in file.readlines():
            list.append(clean_line(line, list))
    list.sort()

def clean_line(line, list):
    line = line.strip('\n')
    while '' in list:
        list.remove('')
    return line

def create_new_file(list, path):
    with open(path, 'w') as file:
        for song in list:
            file.write(song + '\n')

def main():
    new_path = 'C:/Users/jovan/Documents/Python//final_doc.txt'
    path = 'C:/Users/jovan/Documents/Python//canciones_ejercicio.txt'
    list = []

    read_file(path, list)
    create_new_file(list, new_path)

main()