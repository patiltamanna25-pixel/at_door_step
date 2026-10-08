def add(*args):
    total=0
    for i in args:
        total+=i
    return total

def sub(*args):
    sub=0
    for i in args:
        sub=i-sub
    return sub

def mul(*args):
    mul=1
    for i in args:
        mul=mul*i
    return mul

def div(*args):
    div=args[0]
    for i in args[1:]:
        div=div/i
    return div

def rem(*args):
    rem=args[0]
    for i in args[1:]:
        rem=rem%i
    return rem

print("******************* | BASIC CALCULATOR | ***********************")
print("Number of values you want to calculate?")
num = int(input())

li = []
print("Enter values one by one")
for i in range(num):
    val = int(input())
    li.append(val)

print("Enter your Operator(+,-,*,/,%)")
op = input()

tup = tuple(li)
if(op == '+'):
    print("Sum is: ",add(*tup))
elif(op == '-'):
    print("Difference is: ",sub(*tup))
elif(op == '*'):
    print("Product is ",mul(*tup))
elif(op == '/'):
    print("Division is ",div(*tup))
elif(op == '%'):
    print("Remainder is ",rem(*tup))
else:
    print("ERROR: INVALID OPERATOR")


