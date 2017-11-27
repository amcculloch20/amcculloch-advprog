class Circle():
    def __init__(self, r):
        self.x = r

    def area(self):
        return (self.x**2)*3.14

    def perimeter(self):
        return 2*self.x*3.14

    def __str__(self):
        return "Circle has a radius of %.2f, an area of %.2f, and a perimeter of %.2f" % (self.x, self.area(), self.perimeter())

class Rect():
    def __init__(self, l, w):
        self.x = l
        self.y = w

    def area(self):
        return x*y

    def perimeter(self):
        return 2*y + 2*x

    def __str__(self):
        return "Rectangle has a length of %.2f and a width of %.2f. It has an area of %.2f and a perimeter of %.2f" %(self.x, self.y, self.area(), self.perimeter())

circle1 = Circle(5)
rect1 = Rect(3,2)

print circle1
print rect1
