#plymorphism (run time)
class Shape():
    def area(self):
        return 0
class Circle(Shape):
    def area(self):
        return 3.14*5*6
class Rectangel(Shape):
    def area(self):
        return 20*20
shapes=[Circle(),Rectangel()]
for Shape in shapes:
    print (Shape.area())

#duck type (dynamic type) polymorphism
class Bird:
    def fly(self):
        print("bird can fly")
class Airplan:
    def fly(self):
        print("Airplan can fly")
def lets_fly(flying_thing):
    flying_thing.fly()

b=Bird()
a=Airplan()
lets_fly(b)
lets_fly(a)  #no need of inheritance-just same method name


#Opeator overloading
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages+ other.pages
b1=Book(200)
b2=Book(150)
print(b1+b2)

#function overloadinng (not directlu suppoerted use *args or defult value )
#method 1 : Defult argument
def greet(name="welcome"):
    print("priya",name)
greet()
greet("diya")

#method2: using *ags
def add(*number):
    result=0
    for num in number:
        result+=num
    return result
print(add(2,4))
print(add(1,2,3,4,5))

#method 3:using type checking
def display(data):
    if isinstance(data,int):
        print(data)
    elif isinstance(data,str):
        print(data)
    else:
        print("unkown type")
display(10)
display("hi")
display(10.4)
