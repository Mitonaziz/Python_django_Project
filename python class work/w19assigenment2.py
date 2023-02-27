#Write a Python program that inputs three integers and calculates and prints out their sum. However, if the three numbers are all equal then print out three times their sum.
num1=int( input("1st number = "))
num2=int(input("2nd number = "))
num3=int(input("3rd number = "))
sum=(str(num1+num2+num3))

if num1==num2 and num2==num3:
    print("sum valu is "+sum)
    print("sum valu is "+sum)
    print("sum valu is "+sum)
else:
    print("Total sum = "+sum)
    
#Write a Python program that takes in an input of an integer grade. Based on the following, print out the corresponding letter grade:
grade = input( )
           