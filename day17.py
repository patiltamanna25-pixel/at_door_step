#1.1.	Combine two lists using zip(): 
# names = ["A", "B", "C"]
# marks = [90, 80, 70]
names = ["A", "B", "C"]
marks = [90, 80, 70]
res=zip(names,marks)
print(list(res))
#2.2.	Print index and value using: enumerate()
# fruits = ["apple", "banana", "mango"]
fruits = ["apple", "banana", "mango"]
for index, fruit in enumerate(fruits):
    print(index,fruit)
#3.	Check if any number is negative using any():nums = [1, 2, -3, 4] 
nums = [1, 2, -3, 4]
print(any(nums))
# or nums = [1, 2, -3, 4]
# result = any(n < 0 for n in nums)

# print(result)  # Output: True
#3.4.	Check if all numbers are even using all(): 
# nums = [2, 4, 6, 8]




