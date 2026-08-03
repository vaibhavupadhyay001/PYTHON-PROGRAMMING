




class person:
    name="anonymous"

    def ChangeName(self , name):
        self.name=name

p1=person()
p1.ChangeName("Vaibhav upadhyay") # it will change inside the object , not insode the class...
print(p1.name)
print(person.name)




#inside class chnage #1

class person:
    name="anonymous"

    def ChangeName(self , name):
        person.name=name # it will chnage inside the class 

p1=person()
p1.ChangeName("Vaibhav upadhyay") # it will change inside the object , not insode the class...
print(p1.name)
print(person.name)


#inside class chnage #2

class person:
    name="anonymous"

    def ChangeName(self , name):
        self.__class__.name="Vaibhav" # it will chnage inside the class 

p1=person()
p1.ChangeName("Vaibhav upadhyay") # it will change inside the object , not insode the class...
print(p1.name)
print(person.name)




## A class method is bound to the class and receives the class as an implicit first arguement
# Static method cann'nt access or modify class state & generally for utility

# @classmethod

class Person:
    name="Abhay"

    @classmethod
    def changename(cls , name):
        cls.name=name
p1=Person()
p1.changename("rahul kumar")
print(p1.name)
print(Person.name)



#methods are of 
#static
#class
#instance
