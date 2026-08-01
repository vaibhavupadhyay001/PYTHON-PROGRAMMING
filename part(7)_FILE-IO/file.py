#python can be used to perform operations on a file ( read and write data)

#there are two type of files
# 1 . text files (.txt , .docx , .log etc)
# 2. Binary files (mp4 , .mov , .png , .jpeg)

# open , read & close file 

# we have to open the file before reading 
# f=open("file_name" , "mode")
# data = f.read()
# f.close()

f=open("part(7)_FILE-IO/demo.txt" , "r") # r , w , x , a , b , t , + , they are modes
data=f.read()
print(data)
print(type(data))

# x create a new file and open it for writing
# + opens a disk file for updating ( reading an d writing).....
# read()  , reads the entire file ..
# readlne() , reads one line at a time..

line1=f.readline() # read() reads the entiree file so data is remainig if we,re using readline then it will return NULL values
print(line1)


line2=f.readline()
print(line2)

f.close()
