#list
Name =["Azizur","Nasim","emon","Sajed","Sajed"]
print(Name)
print(Name [1:3])#print 1 and 3
print(Name [1:]) #2nd to last print
print(Name [:3])#1st to 3 pirnt

print("The number is ",+ Name.count("Sajed"))
print("The index is ",+Name.index("Sajed"))

#insert
Name.insert(1,"Fatema")
print("After insert", Name)

#Delet
Name.pop(1)
print(Name)
#Remove another way 
Name.remove("Sajed")
print("After Remove",Name)
#Reverse
Name.reverse()
print(Name)

#sort
Name.sort()
print(Name)
#cope
Name2= Name.copy()
print(Name2)

id= ["Azizur",14,"Namim",30]
print(id)
print(id[1])
id[1]=20
print(id)
print(len(id))
#id.clear()
#print(id)
