"""
import re
txt = "Faizan is absent from last few classes"
x=re.findall("a",txt)
print(x)
x=re.search("as",txt)
print(x.start())
print(x.end())

x=re.split("\s",txt)
print(x[5])

x=re.sub("Faizan","Faheem",txt)
print(x)



txt = "{0} is absent from last few classes. {0} have to work hard"

print(txt.format("Faheem"))
#print(txt.format("Faizan"))
#print(txt.format("Silent Students"))

txt = "{Student1} is absent from last few classes. {Student2} have to work hard"
print(txt.format(Student2="Faheem",Student1="Faizan"))


try:
    print(x)
except NameError:
    print("Name Error Exception has occured")
except:
    print("An Exception has occured")


try:
    print(x)
except:
    print("An Exception has occured")
finally:
    print("Program Run Successfully")
    

x=45
try:
    print(x)
except:
    print("An Exception has occured")
else:
    print("Program Run Successfully")


try:
    print(x)
except:
    raise NameError("Please Define X")

x="Hello"
if not type(x) is int:
    raise TypeError("X should be int")
"""
username = input("Enter username:")
print("Username is: " + username)
"""
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
"""