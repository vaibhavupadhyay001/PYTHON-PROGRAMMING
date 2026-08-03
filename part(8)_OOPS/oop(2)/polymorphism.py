#when the same operator is allowed to have diffrent meaning according to the context
# opearators & dunder functions
# a_._sub__(b)
# a.__add__(b)

# more about decorators Getter & setter


#operator overloading

print(1+2)
print("vaibhav " + "BBDITM")
print([1,2,3,4] + [6,7,8,4])

#diffrent data ke according diffrent output aayega .. thats polymorphism....

class complex:
    def __init__(self ,real,img):
        self.real=real
        self.img=img 

    def showNumber(self):
        print(self.real,"i +",self.img,"j")  

    def __add__(self,num2): #dunder function...
        newReal=self.real+num2.real
        newImg= self.img+num2.img
        return complex(newReal , newImg)    



    def __sub__(self,num2): #dunder function...
            newReal=self.real-num2.real
            newImg= self.img-num2.img
            return complex(newReal , newImg)    

num1=complex(1 , 3)
num1.showNumber()   


num2=complex(4 , 6)
num2.showNumber()

num3=num1-num2
num3.showNumber()
