class Employee:

    def __init__(self, id, name, salary):

        self.id = id
        self.name = name
        self.salary = salary

    def __str__(self):

        return self.name

    def __repr__(self):

        return f"Employee(id={self.id}, name='{self.name}', salary={self.salary})"


e = Employee(101,"Abhay",50000)
print(e)
print(repr(e))

print()




class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def __str__(self):

        return f"{self.name} ({self.age})"

    def __repr__(self):

        return f"Student(name='{self.name}', age={self.age})"


s1 = Student("Abhay",20)

print(s1)

print(str(s1))

print(repr(s1))