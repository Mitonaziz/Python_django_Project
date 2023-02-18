#1 Write a Python program that inputs a user's first and last name and prints them in reverse order with a space in between.For example, if the program inputs the first name "Joe" and the last name "Bakers," it should output:Bakers Joe
#ANS 01
firstName = input("first_name is ")
lastName =input("Last name is ")
print("My name is "+firstName+" "+lastName)

#Write a Python program that inputs two integers and prints out the sum of the integers.
#Ans 02
firstintnum =int( input ("Enter your 1st int num "))
secondintnum= int (input("Enter your 2nd int num "))
sum=("sumation of two number is "+str(firstintnum + secondintnum))
print( sum)

#03 A farmer has three species:Chickens = 2 legs Cows = 4 legs Pigs = 4 legs Write a Python program that takes in the number of chickens, cows, and pigs (respectively) a farmer has. Print out the sum of the legs across all animals.
#ans03
Chickens = int(input("Chickens ")) 
cows = int(input("cows "))
pigs = int(input("pings "))
count=(Chickens+cows+pigs)
print("The sum of the legs across all animals "+(str(count)))
