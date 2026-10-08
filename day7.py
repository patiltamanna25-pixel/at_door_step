#1.	Print numbers from 1 to 10 using a loop.
for i in range(1,11):
    print(i)
#2.	Print all even numbers from 1 to 50. 
for i in range(1,50):
    if i%2==0:
        print(i)
#1.	Take a number from user and check: 
# o	if it is even or odd 
n=int(input("Enter the number:"))
for i in range(n):
    if i%2==0:
        print("number is even ")
    else:
        print("ODD number ")
    
