"""
def my_function():
    print ("My Name is Adnan")

my_function()

def my_name(fname):
    print("My name is " + fname)

my_name("Adnan")
my_name("Faizan")

def my_name(fname, lname):
    print("My name is " + fname +" "+ lname)

my_name("Adnan","Ansari")

def my_function(*kids):
  print("The youngest child is " + kids[-1])

my_function("Rida", "Rayyan", "Hamdan")

def my_function(child3,child2,child1):
    print("The eldest child is " + child1)
    
my_function(child2="Rayyan", child1="Rida", child3="Hamdan")
my_function("Rida", "Rayyan", "Hamdan")

def my_function(child3 = "Rida",child2 = "Hamdan",child1 = "Rayyan"):
    print("The eldest child is " + child1)
    
my_function()
my_function("Rida", "Rayyan", "Hamdan")
my_function(child2="Rayyan", child1="Rida", child3="Hamdan")


def my_function(fruit):
    for x in fruit:
        print(x)
        
fruits=["apple", "banana", "oranges"]
my_function(fruits)

def Percent(Marks):
    return (Marks/50)*100
    return ("XYZ")
print(Percent(20))


x= Percent(15)+10
print(x)

"""

def recursive_function(k):
    if(k > 0):
        result = k + recursive_function(k-1)
        print(result)
    else:
        result = 0
    return result
    
recursive_function(4)

def rest():
    pass


