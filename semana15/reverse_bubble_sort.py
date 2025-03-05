'''
This one is just something that made me curious to 
know if it could be done, 
and it ended up working. 
'''


def bubble_sort(list_to_sort):
    for big_index in range(len(list_to_sort) - 1, 0, -1):
        for index in range(len(list_to_sort) - 1, 0, -1):
            current_value = list_to_sort[index]
            next_value = list_to_sort[index - 1]
            if current_value > next_value:
                list_to_sort[index] = next_value
                list_to_sort[index - 1] = current_value

list_to_sort = [37, 92, 15, 48, 76, 23, 89, 5, 64, 31]

bubble_sort(list_to_sort)

print(list_to_sort)