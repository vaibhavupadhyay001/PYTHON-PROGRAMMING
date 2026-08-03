#when one class (child / derived) derives the properties & methods of another class (parent/base).
# eg class Car & class Toyota_Car ..

class Car:
    color="black"
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("car stopped..")



class ToyotaCar(Car):
    def __init__(self , name):
        self.name=name


car1=ToyotaCar("fortuner")
car2=ToyotaCar("prius")

print(car1.start())
print(car1.stop())
print(car1.color)

#types of inheritance 
#Single inheritance 
#multi-level Inheritance
#Multiple inheritance



class Car: # thats multi level inheritance ...
    color="black"
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("car stopped..")


class ToyotaCar(Car):
    def __init__(self , brand):
        self.brand=brand

class fortuner(ToyotaCar):
    def __init__(self, type):
        self.type=type



car1=fortuner("diesel")
car1.start()



# multiple inheritance
# a child class can inherit property of more than one parent class...

class A:
    varA="welcome to class A"

class B:
    varB="welcome to class B"

class C(A,B):
    varC="welcome to class C"  


c1=C()

print(c1.varA)
print(c1.varB)
print(c1.varC)




### ______SUPER MATHOD _____###

class Car:
    def __init__(self , type):
        self.type=type

    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("car stopped..")



class ToyotaCar(Car):
    def __init__(self , name , type):
        self.name=name
        super().__init__(type)
        super().start()


car1= ToyotaCar("fortuner","petrol")
print(car1.type) # can not be accesed without super class ..       


      

