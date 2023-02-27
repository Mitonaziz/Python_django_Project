#a Student fails the course if their attendance is less than 75% Take the following inputs :number of classs held and number of classes attended .print out: the stdents attendace and if they failed the course
total= int(input("Number of class held "))
attended=int(input("Number of class attended"))
attendence= round(attended/total , 2)
print("Attendence = "+str(attendence))
if (attendence<0.75):
    print("they fail the course")
    
else:
    print("not fail")
