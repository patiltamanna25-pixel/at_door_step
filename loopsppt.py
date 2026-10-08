fruits=["Apple","Mango","Grapes","Banana"]
for i in fruits:
    print(i)
i = 1
while i<=10:
    print(i)
    i+=1
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 4:
        print("Found 4! Stopping the loop.")
        break
    print(f"Checking number: {num}") 



for num in range(1, 6):
    if num % 2 != 0:
        # Skip odd numbers
        continue
    print(f"Even number found: {num}")
for num in range(1, 4):
    if num == 2:
        pass 
    print(f"Processing: {num}")   
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)   


# Change this number to make the stairs bigger or smaller
rows = 10
for i in range(1, rows + 1):
    print("*" * i)   