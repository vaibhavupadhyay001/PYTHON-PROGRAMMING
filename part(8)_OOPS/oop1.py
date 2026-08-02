#to map with real world scenarios , we started using objects in code.
#this is called objects oriented programming.
#procedural -> functional -> OOP 

# class is a blueprint for creating a objects 
class Student:
     #name = "karan" # class
     def __init__(self , fullname , marks): #parametrized constructors
        self.name=fullname #creates a variable inside class...
        self.marks=marks
        print("adding new stident to the database")
   
s1=Student("vaibhav" , 97) # this parenthesis is calling the constructor
print(s1.name , s1.marks) # object
s2=Student("Abhay" , 89)
print(s2.name , s2.marks)

#the data that is stored inside the class or objects are called attributes






class Car:
    color="Blue"
    brand="tata"

car1=Car()
print(car1.brand)   
print(car1.color) 


#__constructor__
#all classes have a function called _init_() , which is always execueted which is always exexuted when the object is beaing initiated..
