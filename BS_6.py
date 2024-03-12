"""
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name} {self.age}"

p2 = person("Adnan",34)
print(p2.name)
p3 = person("Shahbaz",24)
print(p3.name)


print(p2)
print(p3)

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
        
    def Welcome(self):
        print("Hello my name is " + self.name)
        
p2 = person("Adnan",34)
p2.Welcome()

print(p2.age)
p2.age = 40
print(p2.age)
del p2.age
print(p2.age)


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("Adnan", "Ansari")
x.printname()

class Student(Person):
    def __init__(self, fname, lname):
        self.firstname = lname
        self.lastname = fname

x = Student("Adnan", "Ansari")
x.printname()

"""


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("Adnan", "Ansari")
x.printname()

class Student(Person):
    def __init__(self, fname, lname, year):
#        Person.__init__(self, fname, lname)
        super().__init__(fname, lname)
        self.graduationyear = year
    def Welcome(self):
        print(self.firstname, " ", self.lastname, " ", self.graduationyear)

x = Student("Adnan", "Ansari",2019)
x.printname()
print(x.graduationyear)
x.Welcome()
