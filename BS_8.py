"""import BS_Module
BS_Module.greeting("Adnan")
print(BS_Module.person1["age"])

import BS_Module as B
B.greeting("Adnan")
print(B.person1["age"])

from BS_Module import greeting as B
B("Adnan")


import platform
x=platform.system()
print (x)

x=dir(platform)
print (x)

x= platform.python_version()
print(x)

import datetime as dt
x= dt.datetime.now()
print(x)

print(x.year)
print(x.month)
print(x.strftime("%p"))

x=dt.datetime(2024,4,11)
print(x)
print(x.strftime("%A"))
x=dir(dt)
print(x)

x=min(10,15,20,5,3,2)
y=max(10,15,20,5,3,2)
print(x)
print(y)

x=abs(-5)
print(x)

x=pow(4,3)
print(x)

import math

x=math.sqrt(64)
print(x)

x=math.pi
print(x)


"""
#Regex in python
import re
txt = "Faizan is absent from last few classes"
x=re.search("last", txt)
print(x)

x=re.split("\s",txt,1)
print(x)