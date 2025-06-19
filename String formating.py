#% operator
city=input("Enter City: ")
year=int(input("Enter year:"))
print("I vist %s in %d."%(city,year))
#f-string method 
name=input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello{name},you are{age}years old")
#format method
product=input("enther the product name:")
price=float(input("Enter price:"))
print("The {} costs ${:.2f}".format(product,price))