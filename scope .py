x="Global"
def outer():
    x="enclosing"
    print("inside outer()",x)
def inner():
    x="Local"
    print("inside inner()",x)
inner()
outer()
    
print(len("hello"))

print("Global",x)
