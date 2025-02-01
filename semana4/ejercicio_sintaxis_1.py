name = input('Type your name: ')
last_name = input('Type your last name: ')
age = int(input('Type your age: '))

age_list = [
    "Baby",
    "Child",
    "Tween",
    "Adolescent",
    "Young adult",
    "Adult",
    "Elderly"
]

if age < 2:
    result = age_list[0]    
elif 2 <= age <= 11:
    result = age_list[1]
elif 11 < age <= 12:
    result = age_list[2]
elif 12 < age <= 19:
    result = age_list[3]
elif 19 < age <= 35:
    result = age_list[4]
elif 35 < age <= 64:
    result = age_list[5]
else:
    result = age_list[6]

print(f"The person with the name {name} is a {result}.")
