# practice py 

class Student():
    def __init__(self,fullname ,marks):
        self.name=fullname
        self.marks=marks

    def avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hy", self.name,"your avg score avg is" , sum/3)
    

s1=Student("vaibhav" ,[97,18,99])
print(s1.name , s1.marks)
s1.avg()

s1.name="Abhay"
s1.avg()
