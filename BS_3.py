#Tuples
'''
    1. Ordered collection of elements
    2. Round brackets ()
    3. Can store different data types
    4. Unmutable
'''
'''
tup1=(1,"biryani",5.002,True)
print(tup1[2])

print(type(tup1))

print(len(tup1))

print(tup1[0:4])

tup2=(2,"Apple",8.006,False)

print(tup1+tup2)

print(tup1*2+tup2)

tup3=(56,25,33,42,21,89,65)
print(min(tup3))
print(max(tup3))

print(tup3*2)
'''
#List
"""
1. Ordered Collection of elements
2. Square brackets []
3. Changeable 
4. Different data types can be stored
"""
'''
List1=[1,"biryani",5.002,True]
print(type(List1))
print(len(List1))
print(List1[1])

List2=[2,"Apple",8.006,False]

print(List1+List2)

List1.reverse()

print(List1)

List1.pop()

print(List1)

List1.append(1)
print(List1)

List1.remove(True)
print(List1)

List3=[56,25,33,42,21,89,65,56,25,33,56]
print(List3.count(56))
List3.sort()
print(List3)

print(List2+List3)

List2.extend(List3)

print(List2)

'''

#Dictionary
"""
1. An unordered collection of elements
2. key and values
3. Declared curly brackets {}
4. Mutatable
"""
'''
dict1={"Apples":300, "Orange":350, "Banana":400, "Strawberry": 250}

print(type(dict1))
print(len(dict1))
print(dict1)

print(dict1["Banana"])
print(dict1.keys())
print(dict1.values())
print(max(dict1.values()))

dict1["Mango"]=600
print(dict1)

dict2={"Besan":200, "ata":150, "Cheeni":120}
print(dict2)

dict1.update(dict2)
print(dict1)
'''

#Sets
"""
1. An unordered and unindexed collection of items
2. Declare curly brackets {}
3. Duplicates not allowed
"""

set1={10,20,"Adnan", "Ansari", "QAU"}
print(type(set1))

set1.add("QAU")
print(set1)

set2={10,"QAU","Bioinfo",55,False}
print(set1.intersection(set2))
print(set1.union(set2))