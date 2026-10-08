import numpy as np

arr = np.array([[
[85, 90, 88, 92],
[70, 65, 72, 75],
[95, 98, 94, 99]
]])

# last column fetch
# last value eg 99
# and also 2 row ka 3rd element
# [88 92
#  72 75]
# last row
# 2nd column print
#convert it in single dimension
#using negetive indexing print last 5 elements
#using loops print 90 88 65 72 98 94 should be horizontal
# sum of all elementn=[]
lst=[]
for n in range(10):
    if n%2==0:
        lst.append(n)
print(lst)
[x for x in range(10)
 if x%2==0]