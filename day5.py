# 1.	Create a set with 5 numbers and print it.
s={1,2,3,4,5} 
print(s)
# 1.	Create a set from a list:
# lst = [1, 2, 2, 3, 4, 4]
ls=[1, 2, 2, 3, 4, 4]
print(set(ls))
# 3.	Create an empty set and add 3 elements using .add().
s=set() 
s.add(1)
s.add(3)
s.add(4)
#s.remove(1)
#s.discard(3)
print(s)
print(len(s))  #print lenght of set 
#Create two sets and print their union using .union(). 
s1={1,2,3,3,4,5}
s2={1,2,3,3,4,5}
print(s1.union(s2))
print(s1.intersection(s2))
#Function,What it does,Real-world example
# Union,Combines everything.,Everyone in both groups (no duplicates).
# Intersection,Finds common ground.,Only friends who are in both groups.
# Difference,Subtracts one from another.,Friends in Group A who are not in Group B.
#8.	Create a set and clear all elements. 
s={1,2,3,3,4,5}
s.clear()
print(s)
# 9.	Check the type of:
# s = {}
# and explain what it is.
s={}
print(type(s))  #its type is dict because python consider it as empty dictionary not a set..for creating set we need to use set()
st={12,12.2,"Tannu",True,None}
print(st)
#  Intermediate Level (Set Operations)
# 1.	Given:
# A = {1, 2, 3}
# B = {3, 4, 5}
# Find:
# o	Union 
# o	Intersection 
# o	Difference 
A={1,2,3}
B={3, 4, 5}
print(A.union(B))
print(A.intersection(B))
print(B.symmetric_difference(A))
#Find elements present in A but not in B.
#Find symmetric difference between two sets.
#4.Add multiple elements to a set using .update(). 
a=(1,2,3,5,6,7,8,9)
a.update(1,12,16)
print(a) 
