
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
        print "students name is", self.name
        print "students favorite subject is", self.favsub
        print "student's age is ", self.age
        print "student's height is", self.height


    def stunum(self):
        Student.count += 1
        print "student id number is", Student.count

    def which(self):
        if tech == "apple":
            Student.apple +=1
        else:
            Student.samsung += 1
        print Student.apple, "people have apple"
        print Student.samsung, "people have samsung"



while 1:
    x =raw_input("do you want to add a person (y? or n?)")
    if x == "y":
        name = raw_input("What is the students name?")
        height = raw_input("What is the student's height?")
        age = raw_input("What is the students age?")
        favsub = raw_input("What is the students fav subject?")
        tech = raw_input("Apple or samsung?")

        dage = {}
        dage[name] = age

        dheight = {}
        dheight[name] = height

        dfavsub = {}
        dfavsub[name] = favsub
    else:
        break


student1 = Student(name, favsub, age, height)
student1.disstu()
student1.stunum()
student1.which()



print "their ages are", dage
print "their heights are", dheight
print "their favorite subject is", dfavsub
