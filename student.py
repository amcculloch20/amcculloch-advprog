directory = []
class Student:
    count = 0
    apple = 0
    samsung = 0

    def  __init__(self,name,favsub,age,height,sid):
        self.name = name
        self.favsub = favsub
        self.age = age
        self.height = height
        Student.count += 1
        self.sid = Student.count

    """def disstu(self):
        print "Student's name is", self.name
        print "Student's favorite subject is", self.favsub
        print "Student's age is ", self.age
        print "Student's height is", self.height"""


    def which(self):
        if tech == "samsung":
            Student.samsung +=1
        else:
            Student.apple += 1
        print "Student chose", tech

end = 1
while end == 1:
    x =raw_input("Do you want to add a person to the directory? (y? or n?)")
    if x == "y":
        name = raw_input("What is the student's name? ")
        height = raw_input("What is the student's height? ")
        age = raw_input("What is the student's age? ")
        favsub = raw_input("What is the student's favorite subject? ")
        tech = raw_input("Apple or samsung? ")
        sid = 0
        directory.append(Student(name, favsub, age, height,sid))
        student1 = Student(name, favsub, age, height,sid)
        student1.which()
        print "_______________"
    else:
        n = raw_input("Do you want to see a list of students and their information? (y? or n?)")
        if n == "y":
            print "People in the directory (please ignore the 'none's):"
            for person in directory:
                print "_________________"
                print "Name:", person.name
                print "Height:", person.height
                print "Age:", person.age
                print "Favorite subject:", person.favsub
                print "Apple or Samsung:", person.which()
                print "Student ID:", person.sid

        else:
            z = raw_input("Do you want to leave the program? (y? or n?)")
            if z == "y":
                end = 2

print "_________________"
print "The final technology debate total is:"
print Student.apple, "student(s) has/have apple."
print Student.samsung, "student(s) has/have samsung."
