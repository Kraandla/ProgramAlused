"""
Three different shape classes that each calculate the shapes are and perimeter.
"""
class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b
        self.area = side_b * side_a
        self.perimeter = 2 * (side_a + side_b)

class Triangle:
    def __init__(self, side_a, side_b, side_c, height):
        self.area = height * side_b / 2
        self.perimeter = side_a + side_b + side_c

class Circle:
    def __init__(self, radius):
        import math
        self.area = round(math.pi * (radius ** 2),2)
        self.perimeter = round(2 * math.pi * radius,2)


if __name__ == '__main__':
    square = Rectangle(3,5)
    triangle = Triangle(3,4,5,6)
    circle = Circle(3)
    print("Rectangle area is:", square.area)
    print("Rectangle perimeter is:", square.perimeter)
    print("Triangle area is:", triangle.area)
    print("Triangle perimeter is:", triangle.perimeter)
    print("Triangle area is:", circle.area)
    print("Triangle perimeter is:", circle.perimeter)