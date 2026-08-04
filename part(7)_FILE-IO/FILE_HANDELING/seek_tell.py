file = open("student.txt")
print(file.read())
print(file.tell())
file.close()


file = open("student.txt")
print(file.read(2))
file.seek(0)
print(file.read())
file.close()



file = open("student.txt")
file.seek(5)
print(file.read())
file.close()





file = open("student.txt")
print(file.tell())
file.read(3)
print(file.tell())
file.seek(1)
print(file.tell())
print(file.read())
file.close()


with open("student.txt", "r") as file:
    print("Cursor:", file.tell())
    print(file.read(6))
    print("Cursor:", file.tell())
    file.seek(0)
    print("Cursor:", file.tell())
    print(file.read())
print()

with open("student.txt", "r") as file:
    file.seek(7)
    print(file.read())
print()

with open("student.txt", "w+") as file:
    file.write("Python")
    print(file.tell())
    file.seek(0)
    print(file.read())