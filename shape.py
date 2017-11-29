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
        return self.x * self.y

    def perimeter(self):
        return 2*self.y + 2*self.x

    def __str__(self):
        return "Rectangle has a length of %.2f and a width of %.2f. It has an area of %.2f and a perimeter of %.2f" %(self.x, self.y, self.area(), self.perimeter())

class Square(Rect):
    def __init__(self, x):
        self.x = x
        self.y = x

    def __str__(self):
        return "Square has an area of %.2f and a perimeter of %.2f" %(self.area(), self.perimeter())

class Rtri():
    def __init__(self, b,h):
        self.x = b
        self.y = h

    def area(self):
        return (1/2)*self.x*self.y

    def hypo(self):
        return (self.x**2 + self.y**2)**(1/2)

    def perimeter(self):
        return self.x + self.y + self.hypo()

    def __str__(self):
        return "This right triangle has an area of %.2f and a perimeter of %.2f and the hypotenuse of %.2f" %(self.area(), self.perimeter(), self.hypo())

circle1 = Circle(5)
rect1 = Rect(3,2)
square1 = Square(4)
rtri1 = Rtri(3,4)

print circle1
print "----------------------"
print rect1
print "----------------------"
print square1
print "----------------------"
print rtri1
