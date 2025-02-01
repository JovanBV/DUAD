first_list = ['Hay', 'en', 'que', 'iteracion', 'indices','muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util'] 
third_list = []

even_index = 0
odd_index = 0
for index, word in enumerate(first_list+second_list):
    if index % 2 == 1 and even_index < len(second_list):
        third_list.insert(index, second_list[even_index])
        even_index += 1
    else:
        third_list.insert(index, first_list[odd_index])
        odd_index += 1

print(third_list)
