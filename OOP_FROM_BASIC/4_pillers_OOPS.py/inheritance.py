class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} is working")


class Developer(Employee):

    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def work(self):
        super().work()
        print(f"{self.name} is writing {self.language} code")


dev = Developer("Abhay", 50000, "Python")


print(dev.name)
print(dev.salary)
print(dev.language)

dev.work()

print(Developer.mro()) #order of searching