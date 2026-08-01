# a function that calls itself again and again...


# n to 1 (BACKWARD)
def show(n):
    if(n==0):
        return 
    print(n)
    show(n-1)

show(20)    

#forward

def frwd(n):
    if(n==0):
        return # base case , without base case infinite time run hoga and maximum rec depth exedd ho jayegi

    frwd(n-1)
    print(n)

frwd(5)


#Factorial

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)

print(fact(5)) 


# SUM

def sum(n):
    if(n==0):
        return 0
    else:
        return n+sum(n-1)

print(sum(5))  


# LIST ELEMENT PRINT RECURSIVELY

def print_list(list , idx=0):
    if idx==len(list):
        return
    print(list[idx])
    print_list(list , idx+1)


fruits=["mango" , "banana" , "litchi" , "grapes"]

print_list(fruits)

    