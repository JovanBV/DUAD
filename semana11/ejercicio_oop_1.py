class Circle:
    def __init__(self, radius):
        self.radius = float(radius)
        self.area = 3.14 * (self.radius ** 2)
    
circle = Circle(4)
circle_2 = Circle(10)


print(circle.area)
print(circle_2.area)