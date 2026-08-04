print("========== write() ==========")

with open("student.txt", "w") as file:
    file.write("Abhay\n")
    file.write("20\n")
    file.write("Lucknow")

print("Done")

print()

print("========== append ==========")

with open("student.txt", "a") as file:
    file.write("\nPython Developer")

print("Appended")

print()

print("========== writelines() ==========")

students = [
    "Rahul\n",
    "Riya\n",
    "Aman\n"
]

with open("students.txt", "w") as file:
    file.writelines(students)

print("students.txt created")

print()

print("========== read ==========")

with open("students.txt", "r") as file:
    print(file.read())