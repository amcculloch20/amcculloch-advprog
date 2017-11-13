directory = []
class Student:
    count = 0
    apple = 0
    samsung = 0

    def  __init__(self,name,favsub,age,height):
        self.name = name
        self.favsub = favsub
        self.age = age
        self.height = height

    def disstu(self):
        print "Students name is", self.name
        print "Students favorite subject is", self.favsub
        print "Student's age is ", self.age
        print "Student's height is", self.height

    def stunum(self):
        Student.count += 1
        print "Students ID number is", Student.count


    def which(self):
        if tech == "apple":
            Student.apple +=1
        else:
            Student.samsung += 1



while 1:
    x =raw_input("do you want to add a person to the directory? (y? or n?)")
    if x == "y":
        name = raw_input("What is the students name?")
        height = raw_input("What is the students height?")
        age = raw_input("What is the students age?")
        favsub = raw_input("What is the students favorite subject?")
        tech = raw_input("Apple or samsung?")
        directory.append(Student(name, favsub, age, height))
        student1 = Student(name, favsub, age, height)
        print "-----------"
        print "Student's Information:"
        student1.disstu()
        print "Student's ID number:"
        student1.stunum()
        student1.which()

    else:
        break

print Student.apple, "student(s) has/have apple."
print Student.samsung, "student(s) has/have samsung."

print "People in the directory:"
for person in directory:
    print "Name:", person.name
    print "Height:", person.height
    print "Age:", person.age
    print "Favorite subject:", person.favsub
    print "Apple or Samsung:", person.which
    print "---------"
