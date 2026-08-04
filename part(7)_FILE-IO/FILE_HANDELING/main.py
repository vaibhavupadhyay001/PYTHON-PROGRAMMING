# Read mode
file = open("part(7)_FILE-IO/FILE_HANDELING/student.txt", "r")
data = file.read()
print(data)
print(type(data))
file.close()


file = open("part(7)_FILE-IO/FILE_HANDELING/student.txt", "r")
data = file.read(10)
print(data)
print(type(data))
file.close()


file = open("part(7)_FILE-IO/FILE_HANDELING/student.txt", "r")
data = file.readline()
print(data)
file.close()


file = open("part(7)_FILE-IO/FILE_HANDELING/student.txt", "r")
data = file.readlines()
print(data)
print(type(data))
file.close()

# Write mode (⚠️ This will erase the file!)
# file = open("student.txt", "w")
# file.close()

# Append mode
file = open("part(7)_FILE-IO/FILE_HANDELING/student.txt", "a")
print(file)
file.close()

# Create mode
# file = open("new_file.txt", "x")
# file.close()