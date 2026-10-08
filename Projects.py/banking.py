print("----------M-BANKING SYSTEM----------")
print("================================= ")
n=input("Enter the name of account holder;")
print(f"Hello",n,"welcome to Abcd m-Banking App")
a=input("enter the account number:")
i=input("Enter ifsc code:")
if len(a)==14 and len(i)==11:
    print("valid Account details")
else:
    print("Invalid account details")
ps=input("Enter the password:")
ch=print("1.Account details\n2.Transaction details\n3.Check Balance\n4.Account Type\n5.Exit")
c=input("Enter the serial number of the service: ")
if c=="1":
        print("Account Holder's Name:",n)
        print("Account Number:,",a)
        print("IFSC code:",i)
elif c=="2":
     print("")

        


