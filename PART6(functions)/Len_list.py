cities=["delhi ", "lucknow" , "mumbia" , "noida" , "agra"]
heroes=["Ram ","krishna" ,"Bheem"]
def print_len(list):
    print(len(list))

print_len(cities)   
print_len(heroes)

##write the element of list in single line
## factoriel of n

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)

fact(5)    


# USD TO INR

def cur(usd):
    inr=usd*95
    print("USD= " , usd , "INR=" , inr)

cur(4)    


# WAF to odd even 
