# dictionary __ KEY->VALUE pairs (MUTABLE)

marks={"maths":99 ,
       "physics":90 ,
       "chem":88}

print(type(marks) , marks)

marks["physics"]=99

marks["english"]=93 # added at last

print(marks)

print(marks["physics"])

for key in marks:
    print(key , marks[key])
