class Employee:

    company = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Instance method
    def show_details(self):
        return f"{self.name} earns ₹{self.salary}"

    # Class method
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    # Factory method
    @classmethod
    def from_string(cls, data):
        name, salary = data.split(",")
        return cls(name, int(salary))

    # Static method
    @staticmethod
    def is_valid_salary(salary):
        return salary >= 15000


e1 = Employee("Abhay", 50000)

print(e1.show_details())

print(Employee.company)

Employee.change_company("OpenTech")

print(Employee.company)

e2 = Employee.from_string("Rahul,60000")

print(e2.show_details())

print(Employee.is_valid_salary(50000))
print(Employee.is_valid_salary(10000))