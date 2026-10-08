ls=[1,22,33,44,55]
print(ls)
#2
ls.append("Nitika")
ls.insert(2,44)
print(ls)
ls.remove(44)
ls.pop(5)
ls=[1,22,33,44,55]
print(len(ls))
print(ls[0],ls[4])
print(ls[::-1])
print(ls.find(20))
#9.	Count how many times a number appears in a list
#10.Sort a list in ascending and descending order.
ls=[12,23,45,20]
ls.sort()
print(ls)
ls.sort(reverse=True)
print(ls)
#11.Take a list and print only even numbers
ls=[0,1,2,3,4,5,6,7,8,9]
print(ls[0:9:2])
#12.Find the sum of all elements in a list.
ls=[1,2,3,4,5] 
print(sum(ls))
#convert a string into a list 
s="This is a book"
