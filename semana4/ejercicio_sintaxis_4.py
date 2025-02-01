num_classes = int(input('Type how many classes you are taking: '))
counter = 0
counter_passed = 0
counter_failed = 0
grades_passed = 0
grades_failed = 0

while counter < num_classes:
    grade = int(input('Type the grade for the class: '))
    if grade >= 70:
        counter_passed += 1
        grades_passed += grade
    else:
        counter_failed += 1
        grades_failed += grade
    counter += 1

print('------------------------------------')
print(f'You failed {counter_failed} classes')
print(f'You passed {counter_passed} classes')
print('------------------------------------')

print(f'The average for the classes you passed is: {grades_passed / counter_passed}')
print(f'The average for the classes you failed is: {grades_failed / counter_failed}')
print('------------------------------------')
print(f'The average of all grades is: {(grades_failed + grades_passed) / num_classes}')
