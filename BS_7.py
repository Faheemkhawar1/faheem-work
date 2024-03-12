"""
Obj1=("Banana","Orange","Apple")
print(type(Obj1))
myobj=iter(Obj1)
print(next(myobj))
print(next(myobj))
print(next(myobj))

for x in Obj1:
    print(x)
    
myobj=iter(Obj1[0])
print(next(myobj))


myobj=iter(Obj1)
print(next(myobj))
print(next(myobj))
print(next(myobj))


class Number:
    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x=self.a
            self.a += 1
            return x
        else:
            raise StopIteration
        
    
myclass = Number()
myiter = iter(myclass)
    
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

for x in myiter:
    print (x)

def myfunct():
    global x
    x = 300
    print(x)
    
myfunct()
print(x)



def myfunc():
    x = 200
    def innerfunct():
        print(x)
    innerfunct()
myfunc()
"""