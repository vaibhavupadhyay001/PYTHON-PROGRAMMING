print("========== split() ==========")

print("Python Java C++".split())

print("Apple,Banana,Mango".split(","))

print("03-08-2026".split("-"))

print("abhay@gmail.com".split("@"))

print()

print("========== rsplit() ==========")

print("one two three four".rsplit(" ", 1))

print()

print("========== splitlines() ==========")

text = """Python
Java
C++
JavaScript"""

print(text.splitlines())

print()

print("========== join() ==========")

languages = ["Python", "Java", "C++"]

print(",".join(languages))

print("-".join(languages))

print(" ".join(languages))

print()

print("========== partition() ==========")

email = "abhay@gmail.com"

print(email.partition("@"))

print()

print("========== rpartition() ==========")

path = "folder/subfolder/file.txt"

print(path.rpartition("/"))





s = "Python Java C++"

print(s.split())

print(s.split(" ", 1))

print(s.rsplit(" ", 1))

print(",".join(["A","B","C"]))

print(" ".join(["Hello","World"]))

print("apple-orange".partition("-"))

print("folder/file.txt".rpartition("/"))