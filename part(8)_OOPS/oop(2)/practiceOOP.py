class circle:
    def __init__(self , radius):
        self.radius=radius 


    def area(self):
        return 22/7 *self.radius * self.radius 


    def perimeter(self):
        return 2 * 22/7 * self.radius   


c1=circle(21)   
print(c1.area())
    
print(c1.perimeter()) 




class emp:
    def __init__(self , role , dept ,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def showDetails(self):
        print("role is" , self.role)
        print("dept is", self.dept)  
        print("salray is ", self.salary) 


class eng(emp):
    def __init__(self , name , age):
        self.name=name
        self.age=age
        super().__init__("engineer","IT" , 75000)



eng1=eng("Vaibhav", 22)
eng1.showDetails()
         

e1=emp("manager" , "IT" , 10000)
e1.showDetails()




# revise all the concepts of OOPs
f
