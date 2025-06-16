class Parentclass:
    def __init__(self,name):
        self.name=name
    def speak(self):
        pass

class Childclass(Parentclass):
    def speak(self):
        return f"{self.name} barks!"
d1=Childclass("bunny")
print(d1.speak())


#super() method 
class Person:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print(self.name)
        print(self.id)
class Employee(Person):
    def __init__(self,name,id,age):
        super().__init__(name,id)
        self.age=age

p1=Person("krish",12)
print(p1.name,p1.id)
p2=Employee("om",12,34)
print(p2.name,p2.id,p2.age)

#sinlge inheritance
class Parent:
    def __init__(self,name):
        self.name=name
class Child(Parent):
    def __init__(self, name,age):
        super().__init__(name)
        self.age=age
c1=Child("heer",12)
print(c1.name,c1.age)

#multiple inheritance
class Person:
    def __init__(self,salary):
        self.salary=salary
class Employee(Child,Person):  #inherit from singple inheritance and parent class in multilevel inheritance
    def __init__(self, name, age,salary):
        Child.__init__(self,name,age)
        Person.__init__(self,salary)

e1=Employee("priya",18,20000)
print(e1.name,e1.age,e1.salary)

#multilevel inheritance
class  HR(Employee):                             #inhert from employee
    def __init__(self,name,age,salary,department):
        Employee.__init__(self,name,age,salary)
        self.department=department
r1=HR("priya",18,20000,"CE")
print(r1.name,r1.age,r1.salary,r1.department)

#hierarchical inheritance
class Assisman(Child):                      #inherit from child class
    def __init__(self,name,age,team_size):
        Child.__init__(self,name,age)
        self.team_size = team_size
a1=Assisman("om",12,5)
print(a1.name,a1.age,a1.team_size)

#hybrid inheritance
class Seniorman(HR,Assisman):
    def __init__(self,name,age,salary,department,team_size):
        HR.__init__(self,name,age,salary,department)
        Assisman.__init__(self,name ,age,team_size)
s1=Seniorman("riya",23,2000000,"CE",25)
print(s1.name,s1.age,s1.salary,s1.department,s1.team_size)
