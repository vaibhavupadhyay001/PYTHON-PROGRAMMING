class Student:

    school = "ABC School" #class variable
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


s1 = Student("Abhay") #instance variable
s2 = Student("Rahul")
s3 = Student("Riya")

print(s1.name)
print(s2.name)
print(s3.name)

print(Student.school)

print(Student.count)

Student.school = "XYZ School"

print(s1.school)
print(s2.school)

s1.school = "My School"

print()

print("After Shadowing")

print("s1 :", s1.school)
print("s2 :", s2.school)
print("Class :", Student.school)