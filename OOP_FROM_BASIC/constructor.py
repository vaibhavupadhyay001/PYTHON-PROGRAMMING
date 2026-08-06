class Student:

    def __init__(self, name, age, marks):

        self.name = name
        self.age = age
        self.marks = marks


s1 = Student("Abhay", 20, 92)
s2 = Student("Rahul", 21, 88)

print(s1.name)
print(s1.age)
print(s1.marks)

print()

print(s2.name)
print(s2.age)
print(s2.marks)