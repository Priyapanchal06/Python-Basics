# String: Simply, a string in Python is a sequence of characters enclosed in "", '', """ """, or ''' '''.

# Write string
a = "this is a string"
print(a)

# loopijng usind string (for)

txt="hello"
for i in "txt":
    print(i)

#find length of string 

a="this is a string"
print(len(a))

#slicing in string 

this_string="helloworld!"

print(this_string[1:4])

#from  starting 

print(this_string[0:])

#from ending 
print(this_string[:5])

#negative indexing
print(this_string[-4:-2])

#modifying string 
#upper case
print(this_string.upper())
print(this_string.lower())
print(this_string.strip())

#replace
print(this_string.replace("h","j"))
print(this_string.split())
# concatinate

a="hello"
b="python"
c=a+b
print(c)

#sperate them
print(a+"   "+b)

#fromating string 

name="priya"
text="hello my name is " +name
print(text)

#f string 

a="helloworlds"
b=f"{a} i am a student"
print(b)

#escape chatacter : illegal characters in string 
b="20.00"
txt= "i am a student and my name is \"priya\""
print(txt)
print(a.capitalize())
print(a.center)
print(a.upper())
print(a.lower())
print(b.isdecimal())