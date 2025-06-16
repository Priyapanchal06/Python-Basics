#In set true and 1 consider same and false and 0 consider same 
set1={"apple","cherry","banana",True,1,2,"watermalon"}
print(set1)
set2={"apple","kiwi","dregan",False,0,1,"hi"}
print(set2)
print(len(set1))

#type()
print(type(set1))

#set constructor()
thisset=set(("hello","hi","hey"))
print(thisset)
#access items
for i in thisset:
    print(i)

#if item persent in set give true otherwise false
print("apple" in set1)
print("apple"not in set1)

#to add item in set
set1.add("kiwi")
print(set1)

#update()
other_set={"this","is","another","set"}
set1.update(other_set)
print(set1)

#remove():it show error if item not exist
set1.remove("apple")
print(set1)


#discard: it does not shpw error if item not exist
set1.discard("this")
print(set1)

set1.discard("thisis")
print(set1)

#set have pop method to remove item but it remove any item 

#clear()
set1.clear()
print(set1)

#del()
'''del set1
print(set1) '''

#loop
for i in set2:
    print(set2)

#union():combine both all items
set_item1={"item1","item2","item3"}
set_item2={"item4","item5","item6"}
set_item3=set_item1.union(set_item2)
print(set_item3)

#(|)method
set_item3=set_item1|set_item2
print(set_item3)

#to combine multiple sets
myset=set1.union(set2,thisset) #also use (|) myset=set1|set2|thisset
print(myset)

#update()
set1.update(set2)
print(set1)

#intersection(): to insert one set item into other but give only duplicate
set3=set1.intersection(set2)
print(set1)

#also use & to intersection()
set3=set1&set2
print(set3)

#difference()
set4=thisset.difference(set1)
print(set4)

#also use - for difference()
set4=thisset-set1
print(set4)

#symetric_difference
set5=thisset.symmetric_difference(set2)
print(set5)

#^ used for symetric_difference
set5=thisset^set2
print(set5)