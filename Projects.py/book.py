#___________ BOOK STORE MANAGEMENT SYSTEM________________

books = [
    "Python Basics",
    "Data Structures",
    "Machine Learning",
    "SQL Guide",
    "Java Programming",
    "C Programming",
    "Web Development",
    "Artificial Intelligence",
    "Computer Networks",
    "Operating System"
]

while True:
    print("\n====== BOOK STORE ======")
    print("1. View Books")
    print("2. Buy Book")
    print("3. Sell Book")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nAvailable Books:")
        for i in range(len(books)):
            print(i + 1, ".", books[i])

    elif choice == 2:
        book = input("Enter the book name you want to buy: ")

        if book in books:
            books.remove(book)
            print(book, "purchased successfully!")
        else:
            print("Sorry! Book is not available.")

    elif choice == 3:
        book = input("Enter the book name you want to sell: ")

        if book in books:
            print("This book already exists in the store.")
        else:
            books.append(book)
            print(book, "added to the store successfully!")

    elif choice == 4:
        print("Thank you for visiting the Book Store!")
        break

    else:
        print("Invalid Choice! Please try again.")


