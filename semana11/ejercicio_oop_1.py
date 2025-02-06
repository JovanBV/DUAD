import math


'''
This class represents a circle with a given radius and provides a method to calculate its area.
'''
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


'''
This function validates if the input value is positive and numerical. 
If the value is zero, negative, or not a number, it prompts the user to enter a valid value.
'''
def validate_positive_value(value):
    while True:
        try:
            value = float(value)
            if value <= 0:
                value = input('The radius must be positive. Enter a valid value: ')
            else: 
                return value
        except ValueError:
            value = input('Invalid input. Enter a numerical value: ')


def main():
    radius = validate_positive_value(input('Enter the radius of the circle: '))
    circle = Circle(radius)
    print(f"Radius: {circle.radius}, Area: {circle.area()}")


if __name__ == "__main__":
    main()