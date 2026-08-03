




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