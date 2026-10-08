# #tup=(1,23,54,18,16,11,2,2,1,1,1,1,1)
# print(tup.count(1))
# print(tup[2:4:3])
# print(len(tup))
# t=(20,"tannu",23,56,20.2)
# print(t[2:4:3])

# print(t[0])
# print(t[4])
# tup2=("nikita",56,89,97,65,4,65,65,65,5)
# print(tup2.count(65))
# print(tup2[0])
# print(tup2[4])
# t2=(12,11,10,9,8,7,6,5,4,3,2,1)
# print(t2.index(11))
# print(t2.index(4))
# #DICTIONARY QUESTIONS
# #d={"key":"value"}

# #2.	Write a program to:	Add a new key-value pair to a dictionary. 
d1={"Name":"Tamanna",
    "add":"Shimla",
    "age":20,
    "marks":100}
d1["Pass"]=1234
print(d1)
# #Count how many times each character appears in a string using a dictionary.Example: "hello" → {'h':1, 'e':1, 'l':2, 'o':1} 
# Convert two lists into a dictionary.keys = ['a','b','c'], values = [1,2,3] 
ls=['a','b','c']
v=[1,2,3]
a=dict(zip(ls,v))
print(a)
# #6.	Remove a key from a dictionary using: del pop() 
# d1={10:30,
#     20:50,
#     88:20,
#     23:100}
# print(max(d1.items()))

# d1["Pass"]=1234
# del d1["marks"]
# d1.pop("age")
# print(d1)
# #Find the sum of all values in a dictionary. 
# #8.Merge two dictionaries. 
# d1={"name":"armaan"}
# d2={"bday":"April"}
# d1.update(d2)
# print(d1)
s="this is a test"
a=print(input("Enter the word:"))
b=print(input("Enter another word:"))
print("\u2764")   
print("\U0001F40D")    #snake 
#1. Print formatted text using escape sequences
# Take user name as input and print
# Hello Nikita
# Welcome to Python
# (Use \n)
name=input("Enter the name of user:")
print("Hello",name+ "\n welcome to python")
# 2. Tab space formatting

#  Take two inputs: name and age
# Print output like:
# Name:   Nikita
# Age:    20
# (Use \t)
n=input("Enter the name :")
a=input("Enter the age :")
print("name:",n)
print("Age:",a)
# 3. Quote inside string
#  Take a sentence input and print:
# She said, "Your sentence here"
# (Use \")
s=input("Enter your sentence:")
print("she said, Your sentence is here:\n", s)
# 4. Multi-line input display
#  Take a sentence and print it in 3 lines using escape sequence
sentence = input("Enter a sentence: ")
print(sentence, "\n" + sentence, "\n" + sentence)
# Username & Password Formatter
#  Take username and password using input()
# Print:
# User Details:
#     Username: Nikita
#     Password: ******
un=input("Enter the user name :")
p=input("Enter the password:")
print("user details:\n"+"username:",un,"\nPassword:",p,)
# 6. Bill Generator
# Take item name, price, quantity
# Print formatted bill:
# Item:   Apple
# Price:  50
# Qty:    2
# Total:  100
it=input("Enter the item name :")
p=int(input("Enter the price:"))
q=int(input("Enter the quantity:"))
print("formated bill:\n","Item:",it,"\n Price:",p,"quantity:",q,"\n Total:",p*q,)
# 7. Reverse with formatting
#  Take a string input
# Print:
# •	Original string 
# •	Reversed string 
# •	Both on separate lines using \n 
s=input("Enter the string:")
print("original string:",s,"\nreversed string:",s[::-1],)
# 8. Escape sequence challenge
#  Take a string and print:
# First Line
# "Second Line"
#     Third Line
# (Mix of \n, \", \t)
sr=input("Enter the string:")
print("First Line")
# 10. Email Formatter
#  Take name and domain
# Print:
# Your email is: nikita@gmail.com
e=input("Enter the email:")
d=input("Enter the domain:")
print("Your email is:", e+d)
# Pattern with input
#  Take a word input
# Print:
# N
# N\tN
# N\tN\tN
word = input("Enter a word: ")
print(word)
print(f"{word}\t{word}")
print(f"{word}\t{word}\t{word}")
# 13. Password Strength Hint
#  Take password input
# Print:
# •	Length 
# •	Message in new line: 
# Weak Password
# or
# Strong Password
ps=input("Enter the Password:")
l=len(ps)
print(l)
if l<8:
    print("weak password!!!!")
else:
    print("strong Password****")
# 14. Address Formatter
#  Take user address in one line
# Print in format:
# Address:
#     Line1
#     Line2
#     Line3
# a=input("Enter the address:")
# if 
d1="Hello"
print(d1.split())
a=set(map(lambda x:d1.count(x),d1))
print(a)
#.4.	Count how many times each character appears in a string using a dictionary.
#  Example: "hello" → {'h':1, 'e':1, 'l':2, 'o':1}
n = 5

# Upper half
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

# Lower half
for i in range(n, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
    










        










