# def bubble_sort(list_to_sort):  
#     for big_index in range(0, len(list_to_sort) - 1):             O(n)
#         for index in range(0, len(list_to_sort)-1 - big_index):   O(n^2) 
#             current_value = list_to_sort[index]                   O(1)
#             next_value = list_to_sort[index + 1]                  O(1)
#             if current_value > next_value:                        O(1)
#                 list_to_sort[index] = next_value                  O(1)
#                 list_to_sort[index + 1] = current_value           O(1)
#                                                                   El peor caso del algoritmo es O(n^2)
# -----------------------------------------------------------------------------------------------------------

# def print_numbers_times_2(numbers_list):                          
# 	for number in numbers_list:             O(n)
# 		print(number * 2)                   O(1)
#                                           El peor caso es O(n)
# -----------------------------------------------------------------------------------------------------------
#
# def check_if_lists_have_an_equal(list_a, list_b):
# 	for element_a in list_a:                        O(n)
# 		for element_b in list_b:                    O(n*m)
# 			if element_a == element_b:              O(1)
# 				return True                         O(1)
# 	return False                                    O(1)
#                                                   El peor caso es O(n*m), pero si las listas tienen un tamano parecido seria O(n^2)
# -----------------------------------------------------------------------------------------------------------
#
# def print_10_or_less_elements(list_to_print): 
# 	list_len = len(list_to_print)               O(1)
# 	for index in range(min(list_len, 10):       O(1)
# 		print(list_to_print[index]              O(1)
# -----------------------------------------------------------------------------------------------------------
#
# def generate_list_trios(list_a, list_b, list_c):
# 	result_list = []                                                        O(1)
# 	for element_a in list_a:                                                O(n)
# 		for element_b in list_b:                                            O(n*m)
# 			for element_c in list_c:                                        O(n*m*p)
# 				result_list.append(f'{element_a} {element_b} {element_c}')  O(1)
# 	return result_list                                                      O(1)
#                                                                           El peor caso e O(n*m*p), pero si las listas son de tamanos parecidos, seria O(n^3)