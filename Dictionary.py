#create dictionary
thisdictionary={
    "id":"student1",
    "name":"rajeshwari",
    "age":23
}
print(thisdictionary)
print(len(thisdictionary))
#dictionary constructor
dict1=dict(name="raj",age=11)
print(dict1)
#tpe()
print(type(dict1))

#acess item using key 
x=thisdictionary["name"]
print(x)
#also use get() to access item
x=thisdictionary.get("name")
print(x)
#key()
x=thisdictionary.keys()
print(x)

#vlaues()
x=thisdictionary.values()
print(x)

#items
x=thisdictionary.items()
print(thisdictionary)

#change item
thisdictionary["name"]="priya"
print(thisdictionary)

#update()
thisdictionary.update( name="heer")
print(thisdictionary)

#add new item by giveing new key 
thisdictionary["color"]="pink"
print(thisdictionary)

#also use update()
thisdictionary.update({"color":"red"})
print(thisdictionary)

#pop()
thisdictionary.pop("name")
print(thisdictionary)

#popitem()
thisdictionary.popitem()
print(thisdictionary)

dict1.clear()
print(dict1)

#loop for items,keys,values

for x in thisdictionary.keys():
    print(x)

for y in thisdictionary.items():
    print(y)
for i in thisdictionary.values():
    print(i)

#copy()
mydict=thisdictionary.copy()
print(mydict)

#nested dictionary
nesteddict={
"dict1":{
        "name":"priya",
        "age":18
        },
        "dict2" :{
        "name":"Riya",
        "age":19
        },
    "dict3":{
        "name":"krish",
        "age":13
    }
 }
print(nesteddict)
"""yourdict={
    "dict1":dict1,
    "dict2":dict2,
    "dict3":dict3,
}
print(yourdict)"""
print(nesteddict["dict1"]["name"])

#loop nestedloop
for x,obj in nesteddict.items():
    print(x)
    for y in obj:
        print(y+':',obj[y])