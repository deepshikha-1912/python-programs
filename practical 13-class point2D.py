import math

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print("Point:", (self.x, self.y))

    def distance(self, other):
        return math.sqrt(
            (self.x - other.x)**2 +
            (self.y - other.y)**2
        )


p1 = Point2D(2, 3)
p2 = Point2D(5, 7)

p1.display()
p2.display()

print("Distance:", p1.distance(p2))
