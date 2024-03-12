"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists


"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
"""
"""
try:
    f=open("BS_Demo.txt","x")
    f.close()
except:
    print("File already exists!")
f=open("BS_Demo.txt","w")
f.write("Hello! this is BS Biocomputing Class.\n")
f.write("Hello! World\n")
f.write("We are learning Python\n")
f.close()
f=open("BS_Demo.txt","a")
f.write("Hello! this is BS Biocomputing Class.\n")
f.write("Hello! World\n")
f.write("We are learning Python\n")
f.close()

f=open("BS_Demo.txt","r")
#print(f.read(10))
print(f.readline())
print(f.readline())
print(f.readline())
print(f.read())
f.close()

f=open("BS_Demo.txt","r")
print(f.read())


try:
    f = open("bs_demo1.txt", "x")
    f.close()
except:
    print("File don't exists.")
finally:
    f = open("BS_Demo.txt", "r")
    print(f.read())

import os
os.remove("BS_Demo.txt")
#os.rmdir("")

       
""" 
f=open("BS_Demo.txt","w")
f.write("Hello! this is BS Biocomputing Class.\n")
f.write("Hello! World\n")
f.write("We are learning Python\n")
f.close()
f=open("BS_Demo.txt","a")
f.write("Hello! this is BS Biocomputing Class.\n")
f.write("Hello! World\n")
f.write("We are learning Python\n")
f.close()
f=open("BS_Demo.txt","r")
e=open("BS_Demo1.txt","w")
for x in f:
    if "Hello" not in x:
        print(x)
        e.write(x)
e.close()