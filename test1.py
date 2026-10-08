#1.question
ls=[1,2,3,44,5,6,7,43]
print(sorted(ls))
print(ls[7])
#2.Question
def palindrome(text):
    clean_text = ''.join(char.lower() for char in text if char.isalnum())
    return clean_text == clean_text[::-1]
print(palindrome("Racecar"))
print(palindrome("Nitin"))
print(palindrome("121"))
#3.Question . Given a string, count the frequency of each character using a dictionary.
def count_frequency(s):
    frequency= {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
            
    return frequency
text = "vibe coding"
result = count_frequency(text)
print(result)
#4.
n=5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()
#5.
# Write a program that checks whether a number is positive, negative, or zero.
n=int(input("Enter the number:"))
if n>0:
    print("Number is positive")
elif n<0:
    print("Number is negative")
else:
    print("number is zero")
#6.Create a function that takes a list of numbers and returns the sum of only even numbers
ls=[1,2,3,4,5,6]
even=list(filter(lambda x:x%2==0,ls))
print(even)
#7.Create a class Person with attributes name and age.
class Person:
    def __init__(self,name,age):
         self.name=name
         self.age=age
class Student(Person):
    def __init__(self,name,age,studentid):
        self.studentid=studentid
        super().__init__(name,age)
c1=Student("Roop Lal",56,"Piexam")
print("Name is",c1.name,"and age is",c1.age,"student id:",c1.studentid)
#8. Given a list of numbers, separate even and odd numbers into two different lists.
ls=[1,2,3,4,5,6]
even=list(filter(lambda x:x%2==0,ls))
print(even)
odd=list(filter(lambda x:x%2!=0,ls))
print(odd)
#. Find the first non-repeating character in a string.
#    Example input: "swiss"
s = "swiss"
for char in s:
    if s.count(char) == 1:
        print(f"The first non-repeating character is: {char}")
        break
#. Write a function to calculate the factorial of a number.
n=int(input("Enter the number :"))
for i in n:
    if n<0:
        print("negative numbers do not have factorials")
    elif
    

         