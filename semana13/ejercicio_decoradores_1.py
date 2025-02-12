numbers = [42, 87, 13, 59, 24, 76, 35, 91, 8, 67]

def print_and_return(func):
    def wrapper(list):       
        print(list)
        func(list)
        print(func(list))
    return wrapper


@print_and_return
def find_last_of_list(lists):
    return lists[-1]


find_last_of_list(numbers)