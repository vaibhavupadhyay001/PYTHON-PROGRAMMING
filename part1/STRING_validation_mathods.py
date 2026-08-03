print("Python".isalpha())
print("Python123".isalpha())

print()

print("Python123".isalnum())
print("Python@123".isalnum())

print()

print("12345".isdigit())
print("12.5".isdigit())

print()

print("12345".isdecimal())

print()

print("12345".isnumeric())

print()

print("python".islower())
print("Python".islower())

print()

print("PYTHON".isupper())
print("Python".isupper())

print()

print("   ".isspace())
print("Python".isspace())

print()

print("Python Programming".istitle())
print("python Programming".istitle())

print()

print("age".isidentifier())
print("123age".isidentifier())
print("_salary".isidentifier())

print()

print("Python".isascii())
print("こんにちは".isascii())

print()

print("Hello".isprintable())
print("\n".isprintable())




#industry examples
username = "Abhay123"
if username.isalnum():
    print("Valid Username")
else:
    print("Invalid Username")


name = "Abhay"
if name.isalpha():
    print("Valid Name")


text = "     "
if text.isspace():
    print("Invalid Input")


variable = "student_name"
print(variable.isidentifier())    


otp = "458963"
if otp.isdigit():
    print("Correct Format")





print("Python".isalpha())
print("Python123".isalnum())
print("12345".isdigit())
print("12.5".isdigit())
print("python".islower())
print("PYTHON".isupper())
print("   ".isspace())
print("Python Programming".istitle())
print("student_name".isidentifier())
print("123name".isidentifier())
print("Python".isascii())
print("\n".isprintable())



print("12.5".isnumeric())