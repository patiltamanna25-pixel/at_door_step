# Create a multilevel inheritance example using Person → 
#      Employee → Manager
class Person:
    def ask(self):
        print("Person buys the product ")
class Employ(Person):
    def tell(self):
        print("Employ sales the product")
class Manager(Employ):
    def details(self):
        print("manager observe the work ")
m1=Manager()
m1.ask()
m1.tell()
m1.details()
# Show multiple inheritance using Teacher and Researcher
class Teacher:
    def teach(self):
        print("Teacher Teaches skills")
class Scholar(Teacher):
    def skilled(self):
        print("Scholar is skilled enough to teach")
class Researcher(Scholar):
    def search(self):
        print("Researcher search about the information")
r1=Researcher()
r1.teach()
r1.skilled()
r1.search()
#1.	Create a class Animal with method sound(). Create child class Dog and call inherited method. 
class Animal:
    def sound(self):
        print("Animals can speak")
class Dog(Animal):
    def bark(self):
        print("Dog Barks")
d=Dog()
d.sound()
d.bark()
# 2.	Create a parent class Person with attribute name. Create child class Student and print the name. 
#3.	Make a class Vehicle with method start(). Inherit it in class Car. 
class Vehicle:
    def start(self):
        print("Whrringggg")
class Car(Vehicle):
    def instruction(self):
        print("wear a seat belt!!!!!")
c=Car()
c.start()
c.instruction()
#4.	Create class Bird with method fly(). Create child class Parrot. 
class Bird:
    def fly(self):
        print("Birds fly....")
class Parrot(Bird):
    def speak(self):
        print("Parrot gurgles and trills to whistles and squawks")
p=Parrot()
p.fly()
p.speak()
#5.	Create parent class Mobile with method call(). Create child class SmartPhone. 
class Mobile:
    def call(self):
        print("Used only for calling****")
class SmartPhone(Mobile):
    def chat(self):
        print("used for calling and chatting as well****")
s1=SmartPhone()
s1.call()
s1.chat()
# 6.	Create a class Employee with attributes name and salary. Inherit it in Manager. 
#7Make a class Shape with method area(). Create child class Rectangle. 
#8.	Create class BankAccount with method deposit(). Inherit it in SavingsAccount. 
# 6.	Create a class Employee with attributes name and salary. Inherit it in Manager. 
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        # Use super() to inherit name and salary from Employee
        super().__init__(name, salary)
        self.department = department

# Example usage
mgr = Manager("Alice", 90000, "IT")
print(f"Manager: {mgr.name}, Salary: {mgr.salary}, Dept: {mgr.department}")
#8.	Create class BankAccount with method deposit(). Inherit it in SavingsAccount. 
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        """Adds a positive amount to the account balance."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. Current Balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

class SavingsAccount(BankAccount):
    def __init__(self, initial_balance=0, interest_rate=0.01):
        # Use super() to call the constructor of the parent class (BankAccount)
        super().__init__(initial_balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        """Calculates interest and adds it to the balance."""
        interest = self.balance * self.interest_rate
        self.deposit(interest) # Reusing the inherited deposit method
        print(f"Interest added: ${interest}")

# Example Usage
savings = SavingsAccount(1000)
savings.deposit(500)   # Method inherited from BankAccount
savings.add_interest() # Method specific to SavingsAccount



