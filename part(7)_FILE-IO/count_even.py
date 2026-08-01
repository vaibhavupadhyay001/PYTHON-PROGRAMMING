with open("part(7)_FILE-IO/num.txt","r") as f:
    data=f.read()
    print(data)

    nums=data.split(",")
    count=0
    for val in nums:
        if(int(val)%2==0): # count even in a file 
            count+=1
print(count)

    #...withdeaw individual number ..
    #...parse/casting to int

