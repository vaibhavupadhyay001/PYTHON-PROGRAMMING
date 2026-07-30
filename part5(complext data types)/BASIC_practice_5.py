roll_numbers = [101, 105, 102, 101, 108, 105, 110]

unique_rolls = set(roll_numbers)

print("Unique Roll Numbers:")
for roll in unique_rolls:
    print(roll)


    employees = [
    (101, "Alice", 50000),
    (102, "Bob", 65000),
    (103, "Charlie", 45000)
]

search_id = int(input("Enter Employee ID: "))

found = False

for emp in employees:
    if emp[0] == search_id:
        print("Employee Found")
        print("ID:", emp[0])
        print("Name:", emp[1])
        print("Salary:", emp[2])
        found = True
        break

if not found:
    print("Employee Not Found")