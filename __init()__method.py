#__init()__method 
class MyClass:
    def __init__(self):
        print("this is a constructor")
obj=MyClass()

#with parameters
class ThisClass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=ThisClass(20,"priya")
print(p1.age)
print(p1.name)

#self parameter
class Anclass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"this is a self method {self.name} {self.age}")
obj1=Anclass("priya",20)
obj1.display()

#str method 

class Strmethod:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} is {self.age}years old"
str1=Strmethod("priya",20)
str2=Strmethod("krish",19)
print(str1)
print(str2)

#class variable
class ThisVariable:
    variable="none"
    def __init__(self,name,age):
        self.name=name
        self.age=age
v1=ThisVariable("raj",12)
v2=ThisVariable("rutu",13)

print(v1.variable)
print(v1.name)
print(v2.name)

ThisVariable.variable="variable1"

print(v1.name)
print(v2.name)
print(v1.variable)

v1.name="priya"
print(v1.age)
print(v1.name)
