class student:
    def __init__(self , phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        self.percentage =str((self.phy+self.chem+self.math)/3)+"%"


st1=student(98 , 78 , 67)
print(st1.percentage)  

st1.phy=86
print(st1.phy)
print(st1.percentage)




class student:
    def __init__(self , phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
       

    def calculatePercentage(self):
         self.percentage =str((self.phy+self.chem+self.math)/3)+"%"


st1=student(98 , 78 , 67)
st1.calculatePercentage() 

st1.phy=86
print(st1.phy)
st1.calculatePercentage();
print(st1.percentage)



##property


class student:
    def __init__(self , phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math

    @property
    def Percentage(self):
         return str((self.phy+self.chem+self.math)/3)+"%" #automatic chnage in percentage


st1=student(98 , 78 , 67)
print(st1.Percentage)
st1.phy=86
print(st1.phy)
print(st1.Percentage)

    