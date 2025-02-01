my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

first_number = my_list[0]
my_list[0] = my_list[-1]
my_list[-1] = first_number

print(my_list)