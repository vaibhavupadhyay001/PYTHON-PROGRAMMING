print("========== replace() ==========")

text = "banana"

print(text.replace("a", "@"))
print(text.replace("a", "@", 1))
print(text.replace("a", "@", 2))

print()

print("========== strip() ==========")

name = "   Abhay   "

print(name.strip())
print(name.lstrip())
print(name.rstrip())

print()

print("========== strip characters ==========")

print("***Python***".strip("*"))
print("###Python###".strip("#"))
print("$#Python#$".strip("$#"))

print()

print("========== removeprefix() ==========")

url = "https://google.com"

print(url.removeprefix("https://"))

print()

print("========== removesuffix() ==========")

file = "resume.pdf"

print(file.removesuffix(".pdf"))

print()

print("========== Practical ==========")

email = "abhay@gmail.com"

print(email.replace("abhay", "*****"))

phone = "987-654-3210"

print(phone.replace("-", ""))

html = "<br>Hello<br>"

print(html.replace("<br>", ""))

filename = "IMG_photo.png"

print(filename.removeprefix("IMG_"))






s = "   Python Programming   "

print(s.strip())
print(s.lstrip())
print(s.rstrip())

print("banana".replace("a", "*", 2))

print("***Hello***".strip("*"))

print("IMG_001.png".removeprefix("IMG_"))

print("resume.pdf".removesuffix(".pdf"))

print("Python".replace("P", "J"))