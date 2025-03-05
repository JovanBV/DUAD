def turn_string(string):
    result = ''
    for letter in range(len(string)-1, -1, -1):
        result += string[letter]
    return result


def main():
    string_var = "Hello world"
    string_var = turn_string(string_var)
    print(string_var)


main()