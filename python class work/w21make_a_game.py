#Build A guessing game that gives the user 3 tries to guess a number between 1 to 10
secret_num=8
tries=0
gusess=0
while tries<3 and gusess !=secret_num :
   gusess=int(input("Guess a number between 1 to 10 = "))
   tries= tries+1
if secret_num == gusess :
   print("The Number is true")
else :
    print("The Number is not true")   

