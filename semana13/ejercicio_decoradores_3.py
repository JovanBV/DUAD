
class User:
    def __init__(self, birth_date):
        self.birth_date = birth_date

    @property
    def age(self):
        from datetime import date, datetime
        try:
            self.birth_date = datetime.strptime(self.birth_date, '%Y-%m-%d').date()
            today = date.today()
            age = today.year - self.birth_date.year
            if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):  
                age -= 1
            return age
        except:
            raise ValueError('Date format is yyyy-mm-dd')


def verify_if_underage(func):
    def wrapper(age):
        func(age)
        if age <= 18:
            raise ValueError(f'User is underage: {age} years old.')
        else: 
            print(f'User is not underage: {age}')
    return wrapper


@verify_if_underage
def validate_age(user):
    return user


user_1 = User('2009-02-11')

validate_age(user_1.age)



