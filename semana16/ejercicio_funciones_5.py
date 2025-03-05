def find_upper(string_var):
    counter = 0
    for i in string_var:
        if i.isupper():
            counter += 1
    return counter


def find_lower(string_var):
    counter = 0
    for i in string_var:
        if i.islower():
            counter += 1
    return counter


def main():
    input_string = "I Love Nación Sushi"
    upper_count = find_upper(input_string)
    lower_count = find_lower(input_string)
    print(f"There's {upper_count} uppercase letters and {lower_count} lowercase letters")


main()