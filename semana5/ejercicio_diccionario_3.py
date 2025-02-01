person = {
    'name': 'Carlos',
    'age': '28',
    'city': 'Madrid',
    'profession': 'Engineer',
    'hobbies': 'reading, traveling, running',
    'married': 'False'
}
list_of_keys = []

delete_amount = int(input('Type the amount of keys that you want to delete: '))
for i in range(0, delete_amount):
    list_of_keys.insert(i, input(f'Type the {i + 1} key that you want to delete: '))
    person.pop(list_of_keys[i])

print(person)
