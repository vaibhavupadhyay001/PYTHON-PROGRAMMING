#abstraction , hiding the implementaion details of a class and showing the esssentials features to the user



class Car():
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.acc=True
        self.brk=True  
        print("Car started") #unneccessary

car1=Car()
car1.start() # neccesary 



          