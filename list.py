#list length
list12=["apple","banana","cherry"]
print(len(list12))

#list datatype: list allow to differnt datatype in items 
list1=["apple","banana","cherry"]
list2=[1,2,3,4,5]
list3=[True,False,True,False]
list4=["apple",True,45]
print(list1)
print(list2)
print(list3)
print(list4)

#type()
list11=["apple","banana","cherry"]
print(type(list11))

#this constructor: use to create new list
thislist= list(("Apple","cherry","hehheehe"))
print(thislist)

#access item : using index
print(thislist[1])

#negative indexing
print(thislist[-1])

#range of index
print(thislist[1:3])

#check if exist
if "cherry" in thislist:
    print("yes , cherry is exist in list")

#chnage the value of item
thislist[1]="cherry cherry leady"
print(thislist)

#chnage range of item value
thislist[1:2]="fruit1","fruit2"
print(thislist)

#to insert value in list
thislist.insert(1,"fruit0")
print(thislist)

#append : to ad item at the end of list
thislist.append("orange")
print(thislist)

#extend : to add list item in current list from another list
this_is_list=["veg1","veg2","veg3"]
thislist.extend(this_is_list)
print(thislist)

#remove specific item
thislist.remove("Apple")
print(thislist)

#pop 
thislist.pop(0)
print(thislist)
thislist.pop()
print(thislist)

#del 
#del this_is_list
#print(this_is_list) #show error that means successfully deleted

#clear()
this_is_list.clear()
print(this_is_list)

#loop in list
for i in thislist:
    print(i)

#loop through indext number
for i in range(len(thislist)):
    print(thislist[1])

#using while loop
i=0
while i<len(thislist):
    print(thislist[i])
    i =i+1

#sort()
thislist.sort()
print(thislist)

#decending 
thislist.sort(reverse=True)
print(thislist)

#revserse
thislist.reverse()
print(thislist)

#copy()
copylist=thislist.copy()
print(copylist)

#list()
listlist=list(this_is_list)
print(listlist)


