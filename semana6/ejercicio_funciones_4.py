def turn_string(string_var):
    result = ""
    for i in range(len(string_var)-1, -1, -1):
        result += string_var[i]
    print(result)


def main():
    string_var = "Hello world"
    turn_string(string_var)


main()