class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print("2D Point:", self.x, self.y)


class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def display(self):
        print("3D Point:", self.x, self.y, self.z)


p = Point3D(2, 3, 4)
p.display()
