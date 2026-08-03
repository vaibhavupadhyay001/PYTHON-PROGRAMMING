# PYTHON STRING INDEXING & SLICING PRACTICE

s = "Artificial Intelligence"

print("Original String:", s)
print("Length:", len(s))

print("\n================ INDEXING ================")

# Positive Indexing
print("s[0]  =", s[0])
print("s[1]  =", s[1])
print("s[2]  =", s[2])
print("s[5]  =", s[5])
print("s[10] =", s[10])

# Negative Indexing
print("\nNegative Indexing")

print("s[-1] =", s[-1])
print("s[-2] =", s[-2])
print("s[-3] =", s[-3])
print("s[-5] =", s[-5])
print("s[-10] =", s[-10])


print("\n================ BASIC SLICING ================")

# start : stop

print("s[0:5] =", s[0:5])
print("s[1:8] =", s[1:8])
print("s[3:12] =", s[3:12])
print("s[11:23] =", s[11:23])

print("\n================ OMIT START ================")

print("s[:5] =", s[:5])
print("s[:10] =", s[:10])
print("s[:15] =", s[:15])

print("\n================ OMIT STOP ================")

print("s[5:] =", s[5:])
print("s[10:] =", s[10:])
print("s[15:] =", s[15:])

print("\n================ WHOLE STRING ================")

print("s[:] =", s[:])

print("\n================ NEGATIVE SLICING ================")

print("s[-5:] =", s[-5:])
print("s[-10:] =", s[-10:])
print("s[:-1] =", s[:-1])
print("s[:-5] =", s[:-5])
print("s[-15:-5] =", s[-15:-5])

print("\n================ STEP SLICING ================")

print("s[::1] =", s[::1])
print("s[::2] =", s[::2])
print("s[::3] =", s[::3])

print("\n================ START : STOP : STEP ================")

print("s[0:15:2] =", s[0:15:2])
print("s[2:20:3] =", s[2:20:3])
print("s[5:18:2] =", s[5:18:2])

print("\n================ REVERSE ================")

print("s[::-1] =", s[::-1])

print("\n================ NEGATIVE STEP ================")

print("s[::-2] =", s[::-2])
print("s[::-3] =", s[::-3])

print("\n================ REVERSE PART ================")

print("s[15:5:-1] =", s[15:5:-1])
print("s[20:10:-1] =", s[20:10:-1])

print("\n================ COPY ================")

copy = s[:]
print(copy)

print("\n================ FIRST CHAR ================")

print(s[0])

print("\n================ LAST CHAR ================")

print(s[-1])

print("\n================ FIRST 5 CHARS ================")

print(s[:5])

print("\n================ LAST 5 CHARS ================")

print(s[-5:])

print("\n================ REMOVE FIRST CHAR ================")

print(s[1:])

print("\n================ REMOVE LAST CHAR ================")

print(s[:-1])

print("\n================ REMOVE FIRST & LAST ================")

print(s[1:-1])

print("\n================ EVERY SECOND CHAR ================")

print(s[::2])

print("\n================ EVERY THIRD CHAR ================")

print(s[::3])

print("\n================ ODD INDEX CHARS ================")

print(s[1::2])

print("\n================ EVEN INDEX CHARS ================")

print(s[::2])

print("\n================ LAST 10 CHARACTERS ================")

print(s[-10:])

print("\n================ EXCEPT LAST 10 ================")

print(s[:-10])

print("\n================ FIRST 10 ================")

print(s[:10])

print("\n================ MIDDLE PART ================")

print(s[5:15])

print("\n================ REVERSE MIDDLE ================")

print(s[15:5:-1])

print("\n================ EMPTY SLICE ================")

print(s[5:5])

print("\n================ OUT OF RANGE SLICING ================")

print(s[100:])
print(s[:100])
print(s[5:100])
print(s[-100:])

print("\n================ INDEX ERROR EXAMPLE ================")

try:
    print(s[100])
except Exception as e:
    print(e)

print("\n================ PRACTICAL EXAMPLES ================")

email = "abhay@gmail.com"

print("Username :", email[:email.index("@")])
print("Domain   :", email[email.index("@")+1:])

filename = "resume.pdf"

print("Extension :", filename[-3:])
print("Without Extension :", filename[:-4])

phone = "9876543210"

print("Last 4 digits :", phone[-4:])

card = "1234567812345678"

print("Masked Card :", "*"*12 + card[-4:])

url = "https://google.com"

print("Protocol :", url[:5])
print("Website :", url[8:])

name = "Abhay"

print("Reverse :", name[::-1])
print("First 3 :", name[:3])
print("Last 3 :", name[-3:])
print("Without First :", name[1:])
print("Without Last :", name[:-1])