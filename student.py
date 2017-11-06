class Student:

    def  __init__(self,name,favsub,age,height):
        self.name = name
        self.favsub = favsub
        self.age = age
        self.height = height

    def disstu(self):
        print "students name is", self.name
        print "students favorite subject is", self.favsub
        print "student's age is ", self.age
        print "student's height is", self.height

gabe = Student("gabe","programming","15","5'10")

print gabe.disstu()
