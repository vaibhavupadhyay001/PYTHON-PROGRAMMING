f=open("part(7)_FILE-IO/demo.txt","w+")
#f.write("abcde") # overwrite the content of demo.txt
print(f.read()) # abcde ke aage se suru krega padhna
f.close()


# w+ me open krne se file truncate ho jaati hai , old daata read nhi krti , new data write kro then read kregi
 # r+ = read + overwrite and NO TRUNCATE
 # w+ = read + overwrite AND TRUNCATE
 # a+ = read + append and NO truncate


 #______WITH SYNTAX_______
with open("part(7)_FILE-IO/demo.txt","r") as f:
    data=f.read()
    print(data) #NO close

    with open("part(7)_FILE-IO/demo.txt","w") as f:
        f.write("this is vaibhav")
