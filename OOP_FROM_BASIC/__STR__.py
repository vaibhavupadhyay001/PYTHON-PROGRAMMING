#A special (magic/dunder) method that returns a human-readable string representation of an object.
class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def __str__(self):

        return f"Student(Name={self.name}, Age={self.age})"


s1 = Student("Abhay", 20)
s2 = Student("Rahul", 21)

print(s1)
print(s2)

print(str(s1))