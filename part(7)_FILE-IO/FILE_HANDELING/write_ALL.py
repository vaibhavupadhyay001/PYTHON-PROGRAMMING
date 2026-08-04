file = open("part(7)_FILE-IO/FILE_HANDELING/notes.txt", "w")
file.write("Abhay is a softwarere engineeeer\n")
file.write("Rahul")
file.close()


file = open("part(7)_FILE-IO/FILE_HANDELING/notes.txt", "w")
x = file.write("Python")
print(file.write("Hello"))
print(x) # len of python=6

file.close()



file = open("student.txt", "w")

file.write("Abhay\n")
file.write("20\n")
file.write("Lucknow\n")

file.close()



students = [
    "Abhay\n",
    "Rahul\n",
    "Riya\n"
]

file = open("student.txt", "w")

file.writelines(students)

file.close()

