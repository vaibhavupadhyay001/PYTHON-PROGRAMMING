name = "Abhay"
age = 20
cgpa = 8.52345

print("========== f-Strings ==========")

print(f"Name: {name}")
print(f"Age: {age}")
print(f"CGPA: {cgpa:.2f}")
print(f"Upper: {name.upper()}")
print(f"Length: {len(name)}")
print(f"Age after 5 years: {age + 5}")

print()

print("========== Alignment ==========")

print(f"|{name:<10}|")
print(f"|{name:>10}|")
print(f"|{name:^10}|")

print()

print("========== Padding ==========")

print(f"{7:03}")
print(f"{25:05}")

print()

print("========== format() ==========")

print("Name: {}, Age: {}".format(name, age))
print("{:.2f}".format(cgpa))

print()

print("========== % Formatting ==========")

print("Name = %s" % name)
print("Age = %d" % age)
print("CGPA = %.2f" % cgpa)







name = "Python"
price = 123.4567
age = 20

print(f"Hello {name}")
print(f"{price:.2f}")
print(f"{age+10}")
print(f"{name.upper()}")
print(f"|{name:<10}|")
print(f"|{name:^10}|")
print(f"{5:04}")

print("Name: {}, Age: {}".format(name, age))

print("Price = %.1f" % price)