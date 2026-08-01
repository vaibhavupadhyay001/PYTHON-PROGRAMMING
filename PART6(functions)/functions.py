price=100
new_price=price+ (price * 0.18)
print(new_price)
# for diffrent price we have to calculate in manual way 

#to solve this problem fucntions comes in FIELD

def cal_GST(price): #parameters
    new_price=price + (price*0.18)
    print(new_price)

cal_GST(112) # arguements



# IN_BUILT FUNCTION 
#len , min , max , print , type 


##_______MODULE FUNCTION________##
from math import sqrt , log2
print(log2(16))
print(sqrt(81))


import random
print(random.random()) # 0 to 1

print(random.randint(1,10)) # a ,b


# its a block of statment that performs specific task

a=5 
b=10
sum=a+b
print(sum) # redunatant code

#for this we can create a sum fucntion

def sum(a,b): #parameter
    print(a +b ) #function def

sum(100 , 234) #function call and arguments
sum(5,10) #fucntion reduce the reducency 


    