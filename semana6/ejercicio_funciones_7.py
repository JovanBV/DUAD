import math

def delete_even_numbers(number_list):
    for number in range(len(number_list)-1, -1, -1):
        if verify_even_number(number_list[number]):
            number_list.pop(number)
    return number_list


def verify_even_number(number, number_two = 2):
    if number % number_two == 0  and number > 2:
        return True
    else:
        return False


def verify_if_prime(number_list):
    for index in range(len(number_list)-1, -1, -1):
        is_prime = True
        number_verify = number_list[index]
        squared_number = math.ceil(number_verify ** 0.5)
        for number in range(2, squared_number + 1):
            if verify_even_number(number_verify, number):
                is_prime = False
                break
        if not is_prime:
            number_list.pop(index)
    return number_list


def main():
    number_list = [10, 15, 2, 3, 20, 25, 11, 13, 17, 18, 19, 23, 28, 30]
    number_list = delete_even_numbers(number_list)
    number_list = verify_if_prime(number_list)
    print(number_list)
    


main()