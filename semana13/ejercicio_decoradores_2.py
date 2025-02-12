
def validate_numerical_parameter(func):
    def wrapper(*args):
        for parameter in args:
            try:
                int(parameter)
            except:
                raise ValueError('Parameter must be numerical.')
        func(*args)
        print(func(*args))
    return wrapper


@validate_numerical_parameter
def request_user_info(ids, celphone_number, age):
    user_info = [ids, celphone_number, age]
    return user_info


@validate_numerical_parameter
def request_all_students_ages(age_1, age_2, age_3, age_4, age_5):
    students_ages = [age_1, age_2, age_3, age_4, age_5]
    return students_ages


request_user_info(12, 2, 23)
request_all_students_ages(12,'sd',12,12,34)