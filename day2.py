print("hello world")
s="DeepLearning"
print(s[0:11:2])
s="NeuralNetwork"
print(s[1::2])
s="programming"
a=9
b=9
print(a>=b)
print(a<=b)
print(a!=b)
s="NeuralNetwork"
print(s[1:12:2])
s="webdesingning"
s2=s[1:-1]
print(s2)
#12From"ABCDEFGCEGI" using slicing
s="ABCDEFGHI"
print(s[0:9:2])
#13.	Check if a string is a palindrome using slicing. 
#14.From "PythonIsFun", extract "noFsI" using slicing.
s = "PythonIsFun"
s2 = s[5:3:-1] + s[8:5:-1]
print(s2)  # Output: noFsI
#15.Write a program to rotate a string "abcdef" by 2 positions using slicing. 
# Define the initial string
text = "abcdef"
n = 2

# Left Rotation: "cdefab"
left_rotated = text[n:] + text[:n]

# Right Rotation: "efabcd"
right_rotated = text[-n:] + text[:-n]

print(f"Original: {text}")
print(f"Left Rotated by {n}: {left_rotated}ls")
print(f"Right Rotated by {n}: {right_rotated}")
li=[1,2,3,4,5,6,7,8,9]
print(li[::-1])
print(li.count(1))
#16.	From "DataScienceIsAwesome", extract "Science" using slicing only. 
s= "DataScienceIsAwesome"
print(s[4:11])
#17.	Reverse every alternate 3 characters in "ABCDEFGHIJKL". 
s="ABCDEFGHIJKL"



