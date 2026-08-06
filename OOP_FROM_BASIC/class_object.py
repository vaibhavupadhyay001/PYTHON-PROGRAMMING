class Student:
    pass

print(Student)

s1 = Student()
s2 = Student()
s3 = Student()

print(s1)
print(s2)
print(s3)

print(type(s1))

print(isinstance(s1, Student))

print(s1 == s2)

s4 = s1

print(s1 == s4)