#Write a lambda function to find square of a number
sq=lambda a:a*a
print(sq(3))
print(sq(2))
#Use lambda to find maximum of two numbers
max_of_2=lambda a,b:a if a>b else b
print(max_of_2(12,45))
#Filter numbers greater than 10 from a list
ls=[23,21,20,19,18,9,2,3,4]
g=list(filter(lambda x:x>10,ls))
print(g)
#Multiply all elements of a list using reduce()
from functools import reduce
ls=[2,3,4,5,6]
multiply_all=reduce(lambda x,y:x*y,ls)
print(multiply_all)
#1.	Write a lambda function to add two numbers. 
add=lambda a,b:a+b
print(add(2,48))
#3.	Write a lambda to check if a number is even. 
even=lambda a:a%2==0
print(even(10))
#5.	Write a lambda to convert a string into uppercase. 
upper_case=lambda s:s.upper()
print(upper_case("hello world"))
#6.	Use map() to square all numbers in a list. 
ls=[1,2,3,4,5,6,7]
square_all=list(map(lambda x:x*x,ls))
print(square_all)
#7.	Use map() to convert all names into uppercase. 
ls=["nannu","tannu","nitika"]
upper_case_all=list(map(lambda x:x.upper(),ls))
print(upper_case_all)
#8.	Use map() to add 10 to each number in a list. 
ls=[1,2,3,4,5,6,7]
add_10=list(map(lambda x:x+10,ls))
print(add_10)
#9.	Use map() to find length of each word in a list. 
ls=["nannu","tannu","nitika"]
len_of_eachword=list(map(lambda x:len(x),ls))
print(len_of_eachword)
#10.Use map() to convert Celsius temperatures into Fahrenheit. 
temp_in_celsius=[10,20,30,40]
fahrenheit_temps = list(map(lambda c: (c * 9/5) + 32, temp_in_celsius))
print("Temparture in celsius:",temp_in_celsius)
print("Temparture in Fahrenheit:",fahrenheit_temps )
#11.Use filter() to get even numbers from a list.
ls=[1,2,3,4,5,6,7]
even=list(filter(lambda x:x%2==0,ls))
print(even)
#12.Use filter() to get odd numbers from a list. 
ls=[1,2,3,4,5,6,7]
odd=list(filter(lambda x:x%2!=0,ls))
print(odd)
#13.Use filter() to get names starting with "A". 
ls=["Aman","Ajay","Adarsh","Mani","Mohit"]
name_st_with_A=list(filter(lambda x: x.startswith("A"),ls))
print(name_st_with_A)
#14.Use filter() to get numbers greater than 50. 
ls=[13,245,35,46,55,65,70]
greater_50=list(filter(lambda x: x>50,ls))
print(greater_50)
#15.Use filter() to remove empty strings from a list. 
strings = ["apple", "", "banana", " ", "cherry", ""]
result = list(filter(None, strings))
print(result) 
#*********Reduce*********
#16.Use reduce() to find sum of list elements. 
from functools import reduce
ls=[2,3,4,5,6,7,1]
add=reduce(lambda x,y:x+y,ls)
print(add)
#17.Use reduce() to find product of list elements. 
from functools import reduce
ls=[1,2,3,4]
product=reduce(lambda x,y:x*y,ls)
print(product)
#18.Use reduce() to find maximum number in a list. 
from functools import reduce
ls=[1,2,3,4]
max_of_all=reduce(lambda x,y: x if x>y else y ,ls)
print(max_of_all)
#19.Use reduce() to concatenate strings in a list. 
from functools import reduce
ls=["Apple","Grapes","Mango"]
concatenate=reduce(lambda x,y:x+y,ls)
print(concatenate)
#or
from functools import reduce
ls=["Python","is","pretty","awesome"]
concatenate=reduce(lambda x, y: x + " " +y,ls)
print(concatenate)
#20.Use reduce() to count total characters in words list. 
from functools import reduce
words=["Python","is","pretty","awesome"]
count_total_characters=reduce(lambda count,word:count + len((word),words,0))
print(count_total_characters)


from functools import reduce
word = ['h','e','l','l','o']

a = reduce(lambda total,ch:total+1,word,0)
print(a)

 

