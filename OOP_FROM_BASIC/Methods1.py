class Student:

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def show_details(self):
        print("Name :", self.name)
        print("Age  :", self.age)
        print("Marks:", self.marks)

    def update_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.marks = new_marks
        else:
            print("Invalid Marks")

    def greet(self):
        print(f"Hello {self.name}!")


s1 = Student("Abhay", 20, 92)
s2 = Student("Rahul", 21, 85)

s1.greet()
s1.show_details()

print()

s2.greet()
s2.show_details()

print()

s1.update_marks(98)
print("Updated Marks:", s1.marks)

s1.update_marks(120)