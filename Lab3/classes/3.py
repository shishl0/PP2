class Shape:
    def area(self):
        print("Area:", 0) # by default

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area:", self.length * self.width)


rect = Rectangle(4, 6)
rect.area()