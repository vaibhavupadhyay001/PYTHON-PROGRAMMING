#nums=range(10)
#for i in nums:
   # if i%2==0:
     #   print(i , "Even")
   # else:
   #     print(i , "Odd")


        #2 4 6  8 10
      #  for i in range(2 , 11 , 2):
          #  print(i)

            #BREAK

for i in range( 1 , 51):
    if(i==21):
         break
    if(i%3==0):
         print(i)

print("Out of loop") 



for i in range( 1 , 51):
    if(i==21):
         continue
    if(i%3==0):
         print(i)

print("Out of loop") 
