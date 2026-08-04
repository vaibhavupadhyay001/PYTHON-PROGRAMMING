# read()
file = open("part(7)_FILE-IO/FILE_HANDELING/student.txt", "r")

print("===== read() =====")
print(file.read())

file.close()

# read(size)
file = open("part(7)_FILE-IO/FILE_HANDELING/student.txt", "r")

print("\n===== read(5) =====")
print(file.read(5))

print(file.read(5))

file.close()

# readline()
file = open("part(7)_FILE-IO/FILE_HANDELING/student.txt", "r")

print("\n===== readline() =====")
print(file.readline())
print(file.readline())

file.close()

# readlines()
file = open("part(7)_FILE-IO/FILE_HANDELING/student.txt", "r")

print("\n===== readlines() =====")
print(file.readlines())

file.close()