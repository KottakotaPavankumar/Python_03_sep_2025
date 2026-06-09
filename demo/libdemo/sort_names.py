#Create an empty list to store names
names = []
while True:
    name =  input("Enter a name(end to finish): ")
    if name.lower() =="end":
        break
    names.append(name)

#Sort the names alphabetically
names.sort()
with open("names.txt","w") as f:
    for name in names:
        f.write(name+"\n")