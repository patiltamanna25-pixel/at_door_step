print("Hello welcome to the list Manipulator")
li=[1,2,3,4,5,6,7,8,9,10]
ch=input("Do you want to create your own list?(yes/no):")
if ch=="yes":
    li2=[]
    n=int(input("Enter how many elements you want to add:"))
    for i in range(n):
        element=input(f"Enter Element{i+1}:")
        li2.append(element)
    selected_list=li2
    print("Your List:",li2)
elif ch=="no":
    selected_list=li
    print("Your List:",li)
else:
    print("select yes or no")
while True:
    print("\n===== MENU =====")
    print("1. Display List")#to see your list
    print("2. Append Element") #to add element at end 
    print("3. Insert Element") #to insert element at particular index
    print("4. Remove Element") #remove the first occurence of specific element 
    print("6. Pop Last Element")#usually removes and returns the last element
    print("7. Reverse List") #reverse the order of elements in list 
    print("8. Clear List") #removes all elements from the list 
    print("9. Exit")

    choice = int(input("Enter your choice: "))
    if choice==1:
        print("Your List:",selected_list)
    elif choice==2:
        e=int(input("Enter Element to append:"))
        selected_list.append(e)
        print("Updated List:",selected_list)
    elif choice==3:
        
    