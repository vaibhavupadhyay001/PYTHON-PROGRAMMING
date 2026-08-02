#methods are functions that belong to objects

class Student:
     #constructors
     
     def __init__(self , fullname , marks): 
        self.name=fullname 
        self.marks=marks

#methods
     def hello(self):
         print("Hello students" , self.name)

     def get_marks(self):
         print("Mark is " , s1.marks)    
    
   
s1=Student("vaibhav" , 97) 
s1.hello()
s1.get_marks()

