list_count = int(input("Type the amount of lines you want to type for the dictionary: "))
first_list = []
second_list = []
dictionary = {}

for i in range(0, list_count):
    first_list.insert(i, input(f'Type the key name for the value in the {i + 1} position: '))
    second_list.insert(i, input(f'Type the key value for the value in the {i + 1} position: '))
    dictionary[first_list[i]] = second_list[i]

print(dictionary)