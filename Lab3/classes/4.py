import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
p1 = Point(1, 2)
p2 = Point(4, 6)

p1.show()  # (1, 2)
p2.show()  # (4, 6)

p1.move(2, 3)
p1.show()  # (1+2, 2+3) = (3, 5)

distance = p1.dist(p2)
print("Distance between p1 and p2:", distance)