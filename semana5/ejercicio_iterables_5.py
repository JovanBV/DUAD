numbers = [0,0,0,0,0,0,0,0,0,0]

for i in range(len(numbers)):
    numbers[i] = int(input("Type a number: "))

sorted_numbers = sorted(numbers)
print(f'The greatest number in the list is: {sorted_numbers[-1]}')                  