#del keyword
#used to delete object properties or object itself
class Student:
    def __init__(self,name):
        self.name=name

    
s1=Student("Vaibhav")
print(s1.name)
#del s1.name
#print(s1.name)



#private (like) attribute and methods , they are only used within the class and are not accesable from outside the class

class Account:
    def __init__(self , acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass #private

    def reset_pass(self):
        print(self.__acc_pass)    



s1=Account(1234 , 8989)
print(s1.acc_no)
#print(s1.__acc_pass) # private
print(s1.reset_pass())





class Person:
    __name="Vaibhav"

    def __hello(self):
        print("this is a private method")

    def welcone(self):
        self.__hello()   # can be accessed inside the class


p1=Person()
#print(p1.__name)
print(p1.welcone())


