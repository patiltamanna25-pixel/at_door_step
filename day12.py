# #1.	Create a class Student with attributes: name and age. Print the details. 
# class Student:
#  def __init__(self,name,age):
#   self.name=name
#   self.age=age
# s1=Student("Amit",24)
# s2=Student("Arun",22)
# s3=Student("Aryan",22)
# print("Name is",s1.name,"and age is",s1.age)
# print("Name is",s2.name,"and age is",s2.age)
# print("Name is",s3.name,"and age is",s3.age)
# print("Name is",s1.name,"and age is",s1.age)
# #Create a class Car with attributes: brand and model. Create 2 objects and display data. 
# class Car:
#   def __init__(self,brand,model):
#    self.brand=brand
#    self.model=model
# c1=Car("BMW","BMWi3 2026 era")
# c2=Car("Mercedes","Maybach SL 680")
# print("Brand of car is",c1.brand,"and model is",c1.model)
# print("Brand of car is",c2.brand,"and model is",c2.model)
# #3.	Create a class Book with attributes: title and author. Show book details. 
# class Book:
#  def __init__(self,name,author):
#   self.name=name
#   self.author=author
# b1=Book("Rich Dad or Poor Dad","Robert Kiyosaki")
# b2=Book("kill a mocking Bird","Harper Lee")
# print("Name of book is",b1.name,"and Author is",b1.author)
# print("Name of book is",b2.name,"and Author is",b2.author)
# #Create a class Mobile with attributes: company and price. Print mobile info. 
# class Mobile:
#  def __init__(self,name,price):
#   self.name=name
#   self.price=price
# m1=Mobile("I phone 17",90000)
# m2=Mobile("I phone 17 pro Max",125000)
# print("Mobile Info : Phone:",m1.name,"and price of ",m1.name,"is",m1.price)
# print("Mobile Info : Phone:",m2.name,"and price of ",m2.name,"is",m2.price)
# #5.	Create a class Dog with attribute name. Add a method bark() that prints "Woof!". 
# class Dog:
#  def __init__(self,name):
#   self.name=name
#  def bark(self):
#   print("woof")
# d1=Dog("Tommy")
# print(d1.name)
# print(d1.bark())
#6.	Create a class Rectangle with length and width. Find area. 
class Area:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
a=Area(12,5)
a1=Area(3,2)
print("Area  of rectangle is ",a.length*a.breadth)
print("Area  of rectangle is ",a1.length*a1.breadth)
#7.	Create a class Circle with radius. Find circumference. 
class Circle:
    def __init__(self,radius):
        self.radius=radius
pi=3.14
c1=Circle(3)
c2=Circle(2)
print("Radius of circle is:",2*pi*c1.radius)
#8.	Create a class Person with name and city. Print introduction. 
class Person:
    def __init__(self,name,city):
      self.name=name  
      self.city=city
p1=Person("Tamanna","Shimla")
p2=Person("Kartik","chandigarh")
print("Name of person is:",p1.name,"and city is:",p1.city)
print("Name of person is:",p2.name,"and city is:",p2.city)
#9.	Create a class Laptop with brand and RAM. Show details. 
class Laptop:
    def __init__(self,name,storage):
      self.name=name  
      self.storage=storage
l1=Laptop("IdeaPad slim 3","16GB RAM")
l2=Laptop("Dell i3","8GB RAM")
print("Name of laptop is:",l1.name,"and RAM is:",l1.storage)
print("Name of laptop is:",l2.name,"and RAM is:",l2.storage)
#10.Create a class Employee with name and salary. Print employee info. 
class Employ:
    def __init__(self,name,salary):
      self.name=name  
      self.salary=salary
e1=Employ("Tannu",80000)
e2=Employ("Nannu",100000)
print("*******Information of Employs**********")
print("Name of Employ is:",e1.name,"and salary is:",e1.salary)
print("Name of Employ is:",e2.name,"and salary is:",e2.salary)
#1.	Create a class BankAccount with deposit() and withdraw() methods. 
class BankAccount:
    def __init__(self,name,accountnumber):
      self.name=name  
      self.accountnumber=accountnumber
   

    

