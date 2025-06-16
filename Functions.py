#funcation
def my_function():
    print("This is my function")
my_function()

#single argument in function
def my_function(color): #parameter
    print(color+" color") #argument
my_function("green")
my_function("yellow")
my_function("white")

#two arguments
def my_function(fname,lname):
    print(fname+"  "+lname)
my_function("hello","dear")

#arbitary arguments (*args)
def function(*colors):
    print("this is a colors:"+colors[2])
function("yello","white","green","red","pink")

#keyword argument 
def keyword_arg(color3,color2,color1):
    print("good choice is "+color2)
keyword_arg(color1="red",color2="pink",color3="white")

#arbitary keyword argument 
def keyword_value(**kids):
    print("First kid name is:"+kids["kid2"])
keyword_value(kid1="raj",kid2="heer",kid3="yes")

#defult value: when we not pass any argument it pass argument by default
def priya(countrie="india"):
    print("I am from: "+countrie)
priya("rusia")
priya("japan")
priya()
priya("bangulor")

#list of arguments
def function(food):
    for i in food:
        print(i)
fruits=["mango","ornage","cherry","kiwi"]
function(fruits)

#return value
def my_function(i):
    return 5*i
print(my_function(1))
print(my_function(2))
print(my_function(3))
print(my_function(4))

#position only argument 
def my_function(x,/):
    print(x)
my_function(3)

def function(x):
    print(x)
function(3)

#recursion
def banana(k):
    if k>0:
         result=k*banana(k-1)
    else:
        print("not have any value")
        return result
    