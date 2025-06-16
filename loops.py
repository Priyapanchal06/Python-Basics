#while loop
i=1
while i<6:
    print(i)
    i+=1

#break
x = 1
while x<6:
    print(x)
    if x==3:
        break
    x+=1

#continue
y=0
while y<7:
   y+=1
   if y==3:
        continue
   print(y)
else:
   print("end of the loop")

#for loop
items=["Apple","Watermalon","Cherry"]
for x in items:
    print(x)

#range(): automatically increment by one exute iteration by given number,start with o
for i in range(5):
    print(i)

for z in range(4,7):
    print(z)

for r in range(1,10,2):
    print(r)
else:
    print("end of loop")
 
for o in range(1,6):
    if 0==3:
        break
    print(o)
else:
        print("end of loop")


        #recursion
def banana(k):
    if k >0:
        result=k*banana(k-1)
        return result
    else:
        print("not have any value")
        return 1