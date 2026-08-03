text = "banana"

print(text.find("a"))
print(text.find("z"))

print(text.rfind("a"))
print(text.index("a"))

# print(text.index("z"))

print(text.rindex("a"))

print(text.count("a"))
print(text.count("na"))
print(text.count("aa"))

print()

url = "https://google.com"

print(url.startswith("https"))
print(url.startswith("http"))

print()

filename = "resume.pdf"

print(filename.endswith(".pdf"))
print(filename.endswith(".doc"))

print()

email = "abhay@gmail.com"

print(email.find("@"))

print()

sentence = "Python is easy. Python is powerful."

print(sentence.find("Python"))
print(sentence.rfind("Python"))
print(sentence.count("Python"))





s = "Python Programming Python"
print(s.find("Python"))
print(s.rfind("Python"))
print(s.count("Python"))
print(s.find("Java"))
print(s.startswith("Python"))
print(s.endswith("Python"))
print(s.endswith("Programming"))
print(s.find("o"))
print(s.rfind("o"))
print(s.count("o"))