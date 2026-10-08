# #. Create a base class Bird with method fly(). Override fly() in child classes Sparrow and Penguin with different behavior.
# class Bird:
#     def fly(self):
#         print("Most birds can fly high in the sky.")

# class Sparrow(Bird):
#     def fly(self):
#         print("The sparrow flies quickly and chirps along the way!")

# class Penguin(Bird):
#     def fly(self):
#         print("Penguins cannot fly; they are excellent swimmers instead.")

# # Demonstrating the behavior
# s = Sparrow()
# p = Penguin()

# s.fly()  # Output: The sparrow flies quickly and chirps along the way!
# p.fly()  # Output: Penguins cannot fly; they are excellent swimmers instead.
# #Create multiple classes Laptop, Mobile, and Tablet, each having a method price(). Call price() using a loop.
# class Laptop:
#     def price(self):
#         print("Price of Laptop is 50,000 ")
# class Mobile:
#     def price(self):
#         print("Price of Mobile is 1,05,000 ")
# class Tablet:
#     def price(self):
#         print("Price of Tablet is 34,000 ")
# a=Laptop()
# b=Mobile()
# c=Tablet()
# devices = [Laptop(), Mobile(), Tablet()]
# for device in devices:
#     device.price()
#Create an abstract class Vehicle with abstract methods start() and stop(). Implement them in Car and Bike.
from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def start(self):
        print("car started using key!!!")
    def stop(self):
        print("Car stopped using breaks*")
class Bike(Vehicle):
    def start(self):
        print("Bike started using key!!!")
    def stop(self):
        print("Bike stopped using drum breaks*")
c1=Car()
b2=Bike()
c1.start()
b2.start()
c1.stop()
b2.stop()
#7.	Make a class Shape with method area(). Create child class Rectangle. 
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def area(self):
      print("Area=Length*Breadth")
r=Rectangle()
r.area()
#9.	Create a parent class Appliance with method power_on(). Create child class WashingMachine. 
class Appliance:
    def power_on(self):
        print("Electric Appliance is Powered on!!!!")
class WashingMachine(Appliance):
    def power_on(self):
        super().power_on()
        print("Washing Machine is now on")
w=WashingMachine()
a=Appliance()
w.power_on()
#





