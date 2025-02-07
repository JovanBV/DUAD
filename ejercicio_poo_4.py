from abc import ABC, abstractmethod
import math

class Shape(ABC):  
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side_length):  
        self.side_length = side_length

    def calculate_perimeter(self):
        return 4 * self.side_length
    
    def calculate_area(self):
        return self.side_length ** 2

class Rectangle(Shape):
    def __init__(self, length, height): 
        self.length = length
        self.height = height

    def calculate_perimeter(self):
        return self.length * 2 + self.height * 2
    
    def calculate_area(self):
        return self.length * self.height

square_1 = Square(5)
print(square_1.calculate_area())
print(square_1.calculate_perimeter())

rectangle_1 = Rectangle(5, 10)
print(rectangle_1.calculate_area())
print(rectangle_1.calculate_perimeter())

circle_1 = Circle(10)
print(circle_1.calculate_area())
print(circle_1.calculate_perimeter())
