import operator

def request_operator():
    requested_operator = input('Type one of the next options:\n(-) subtracting, \n(+) summary, \n(*) multiplying, \n(/) division, \n(del) To star from zero, \n(close) To close the calculator: \n')
    return requested_operator


def validate_operator(operators):
    while True:
        operator_in_use = request_operator()
        if operator_in_use in operators:
            return operator_in_use
        else:
            print('Type a valid option \n')


def request_value():
    value = input('Type a value: ')
    return value


def validate_value():
    while True:
        value = request_value()
        try:
            value = int(value)
        except ValueError:
            print('Type a numeric value \n')
            continue
        if type(value) == int:
            return value


def main():
    value = 0
    operator_in_use = ''
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, 'close': 'close', 'del': 'del'}
    value = validate_value()
    while operator_in_use != 'close':
        operator_in_use = validate_operator(operators)
        if operator_in_use == 'close':
            break
        elif operator_in_use == 'del':
            value = 0
        print(f'{value} {operator_in_use}')
        value = operators[operator_in_use](value, validate_value())
        print(f'The solution is: {value} \n')


main()