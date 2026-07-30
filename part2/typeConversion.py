age=input("Enter your age: ")
print(age , type(age))
# print(age+1) will give error beacause , string type age

#type conversion 
new_age=int(age)+1
print(new_age)

print(float(new_age))

#do only logical coversion dont convsert ABCD to int

#type conversion VS type casting
#type casting is done by programmer 
#type conversion is done by python interpreter

print(1+2.5) #automatically considering (implicit)
print(1+int(2.999)) #type casting


#______SUM ____ PROGRAM_______#

a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
sum=a+b;

print(sum)


##______String____

name="Vaibhav upadhyay"
grade="B"

#opeartions
print(name.upper()) #it dont affect the original string
print(name.lower())
print(name)

#find
print(name.find("adhy")) # returns positions
print(name.find("tony"))

#replace
print(name.replace("Vaibhav upadhyay" , "Abhay upadhyay"))
print(name.replace("upadhyay" , "Kumar"))

#check the presence
print("V" in name) #true

#reserved words 
#True , in , False , while , for , break , continue...



