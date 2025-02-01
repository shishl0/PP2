class Shape:
    def area(self):
        print("Area:", 0) # by default

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print("Area:", self.length * self.length)

shape_obj = Shape()
shape_obj.area()

square_obj = Square(5)
square_obj.area()