#plymorphism
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