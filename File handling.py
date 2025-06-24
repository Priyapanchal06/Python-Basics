import os
file=open("sample.txt","w")
file.write("Hello world!\n")
file.close()

file=open("sample.txt","r")
print("reading file content: ")
print(file.read())
file.close()

file=open("sample.txt","a")
file.write("Adding a new line at the end.\n")
file.close()
#read again to show addpend content
file=open("sample.txt","r")
print("\n reading after append")
print(file.read())
file.close()

if os.path.exists("sample.txt"):
    os.remove("sample.txt")
    print("\nfile deleted sucessfully")
else:
    print("\n file does not exist")

