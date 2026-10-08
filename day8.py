# Calculator Using Functions
#Addition:
def add(*args):
    total=0
    for i in args:
        total+=i
    return total
#multiplication:
def mul(*args):
    total=1
    for i in args:
        total*=i
    return total
# print(mul())
#subtraction:
def sub(a,b):
    if a>b:
        return a-b 
    else:
        return b-a
print(sub(1,3))
# division:
def div(a,b):
    return a/b
print(div(9,3))
# moudulo:
def div(a,b):
    return a//b
print(div(9,3))
#cube and square:
def sq(n):
    return n*n
def cube(n):
    return sq (n)*n
print(cube(7))
# Prime Number Function
import math

# User-defined function to check primality
def is_prime(num):
    if num <= 1:
        return False
    
    # We only need to check up to the square root of num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False  # Found a factor, so it's not prime
            
    return True  # No factors found, it is prime

# Main block to take user input
user_input = int(input("Enter a number: "))

if is_prime(user_input):
    print(f"{user_input} is a Prime Number.")
else:
    print(f"{user_input} is not a Prime Number.")
#1.	Write a function to print "Hello, World!". 
print("Hello World")
#2.	Create a function that takes a number and returns its square.
#3.6.	Create a function that takes a string and returns it in uppercase
def uppercase(text):
    return text.upper()
s=input("Enter the string:")
print(uppercase(s))
#7.	Write a function to calculate the length of a string without using len(). 
def manual_length(input_string):
    count = 0
    for char in input_string:
        count += 1
    return count
my_text = "Tamanna is learning Python"
print(f"The length is: {manual_length(my_text)}") # Output: 11
#default arguement 
def greet(name="Student"):
    print("Hello",name)
greet()
#Keyword argument 
def add(a,b):
    return a+b
print(add(2,44))
#3parameters
def mul(a,b,c):
    return a*b*c
print(mul(1,2,3))
#
def is_prime(num):
    if num <= 1:
        return False
    
    # We only need to check up to the square root of num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False  # Found a factor, so it's not prime
            
    return True  # No factors found, it is prime
#*___=tuple 
#**=dictionary





















    