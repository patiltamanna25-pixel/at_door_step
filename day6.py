#check whether number is positive or negative
n=int(input("Enter the number:"))
if n>0:
    print("Number is Positive!!!!!")
else:
    print("Number is Negative!!!!")
#check whether number is ]even or  odd
n=int(input("Enter the number:"))
if n//2:
    print("Number is even !!!!!")
else:
    print("Number is odd!!!!")
#greatest of three number
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
n3=int(input("Enter the  third number:"))
if (n1 >= n2) and (n1 >= n3):
    greatest = n1
elif (n2 >= n1) and (n2 >= n3):
    greatest = n2
else:
    greatest = n3
    print(f"The greatest number is: {greatest}")
#GRADE SYSTEM BASED UPON MARKS 
marks=int(input("Enter the marks:"))
if marks>=85:
    print(" CONGRATULATIONS GRADE A")
elif marks>=70:
    print(" CONGRATULATIONS GRADE B") 
elif marks>=60:
    print(" CONGRATULATIONS GRADE C")  
elif marks>=33:
    print(" CONGRATULATIONS GRADE E")
else:
    print("NEED TO WORK HARD fail")
#LOGIN VALIDATION SYSTEM 
usn=input("Enter the name of user:")
ps=input("Enter the password of user which exists in your sytem:")
u=input("Enter the name given by  user:")
up=input("Enter the password given by  user:")
if usn==u and ps==up:
    print("valid user name and password")
else:
    print("unvalid user name and password")







    