#tuple : create
'''allow duplicate item and aloow all datatype'''
thistuple=("Apple","Cheery","Watermalon",123,True,False)
print(thistuple)
print(type(thistuple))
tuple1=tuple(("Apple","banana"))
print(tuple1)

#acess tuple item
print(thistuple[1])
#negative index
print(thistuple[-1])
#range of index
print(thistuple[2:4])

#change value of tuple
x=list(thistuple)
x[2]="kiwi"
thistuple=tuple(x)
print(x)

#append() to aadd item
x=list(thistuple)
x.append("dregan")
thistuple=tuple(x)
print(thistuple)

#tuple to tuple add
x=("item1","item2")
thistuple+=x
print(thistuple)

#remove() to remove items
x=list(thistuple)
x.remove("item1")
thistuple=tuple(x)
print(thistuple)

#del() to remove tuple
'''del tuple1
print(tuple1)'''

#unpacking tuple
(apple,cherry,kiwi,num,flage1,flage2,dregan,item2)=thistuple
print(apple)
print(cherry)
print(kiwi)
print(num)
print(flage1)
print(flage2)
print(dregan)
print(item2)

#loop in tuple
for i in thistuple:
    print(thistuple)

#using index
for i in range(len(thistuple)):
    print(thistuple)

#using while loop
i=0
while i<len(thistuple):
    print(thistuple[i])
    i=i+1

#join two tuple 
tuple2 = tuple1+thistuple
print(tuple2)

#multiple tuple items 
tuple3=tuple2*2
print(tuple3)