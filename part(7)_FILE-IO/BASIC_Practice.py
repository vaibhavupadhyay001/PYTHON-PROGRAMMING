with open("part(7)_FILE-IO/practice.txt" ,"r") as f:
   data=f.read()

new_data=data.replace("Python","Java")
print(new_data)


with open("part(7)_FILE-IO/practice.txt","w") as f:
    f.write(new_data)


 # search if exist or not
def check_for_word(word):
    with open("part(7)_FILE-IO/practice.txt" ,"r") as f:
        data=f.read()
        if(data.find(word)!=-1):
            print("Found")
        else:
            print("Not found")

check_for_word("Jnva")     


#Check for line
def check_for_line(word):
    data=True
    line=1
    with open("part(7)_FILE-IO/practice.txt","r") as f:
        while data:
           data=f.readline()
           if(word in data):
               print(line)
               return
           line+=1

        return -1   


check_for_line(" ") # 3rd line




    

