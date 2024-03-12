"""
i=1
while i<6:
    print(i)
    i+=1
    
i=1
while i<6: 
    print(i) 
    if i==3:
        break  
    print(i)  
    i+=1
    
i=1
while i<6:
    i+=1
    print(i)
    if i==3:
        continue  
    print(i)


i = 1
while i<6:
    print(i)
    i+=1
else:
    print("Out of loop")


fruits=["apple","banana","cherry"]
x=len(fruits)
i=0
while(i<x):
    print(fruits[i])
    i+=1
    

fruits=["apple","banana","cherry"]
for x in fruits:
    if x=="banana":
        continue
    print(x)

for x in fruits[1]:
    print(x)

for x in range(7):
    print(x)


for x in range(3,7):
    print(x)

for x in range(1,7,2):
    print(x)


for x in range(6):
    print(x)
else:
    print("Finally Finished")

"""

Characteristics=["Tasty", "Red", "Yellow"]
fruits=["apple","banana","cherry"]
for x in Characteristics:
    for y in fruits:
        print(x,y)
        
for x in range(3,31,3):
        print(x)
        
for x in [0,1,2]:
    pass