#class and Instance attributes

#class.attr
#obj.attr

class Student:

     college="BBDITM" # same for all stidents(claas sttr)
    
     def __init__(self , fullname , marks):
        self.name=fullname #object attr
        self.marks=marks
        print("adding new stident to the database")
   
s1=Student("vaibhav" , 97) 
print(s1.name , s1.marks , s1.college) 
s2=Student("Abhay" , 89)
print(s2.name , s2.marks , s2.college)

# obj attr > class attribute