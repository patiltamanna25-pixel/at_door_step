def display_menu(menu):
    print("\n--- RESTAURANT MENU ---")
    print(f"{'Item':<15} {'Price':>10}")
    print("-" * 27)
    for item, price in menu.items():
        print(f"{item:<15} ${price:>9.2f}")
    print("-" * 27)

def generate_bill(order_list, menu):
    subtotal = sum(menu[item] for item in order_list)
    tax_rate = 0.08  # 8% tax
    tax = subtotal * tax_rate
    total = subtotal + tax
    
    print("\n--- YOUR FINAL BILL ---")
    for item in order_list:
        print(f"{item:<15} ${menu[item]:>9.2f}")
    
    print("-" * 27)
    print(f"Subtotal:       ${subtotal:>9.2f}")
    print(f"Tax (8%):       ${tax:>9.2f}")
    print(f"Total Amount:   ${total:>9.2f}")
    print("-" * 27)
    return total

def main():
    # 1. Setup the Menu
    menu = {
        "Burger": 12.50,
        "Pizza": 15.00,
        "Pasta": 10.75,
        "Salad": 8.50,
        "Soda": 2.50
    }
    
    order_list = []
    
    while True:
        display_menu(menu)
        choice = input("Enter item name to order (or 'done' to finish): ").title()
        
        if choice == 'Done':
            break
        elif choice in menu:
            order_list.append(choice)
            print(f"Added {choice} to your order.")
        else:
            print("Sorry, we don't have that item. Please try again.")

    # 2. Process Billing
    if order_list:
        total_to_pay = generate_bill(order_list, menu)
        
        # 3. Simple Payment Logic
        while True:
            try:
                payment = float(input(f"Total due is ${total_to_pay:.2f}. Enter payment amount: "))
                if payment >= total_to_pay:
                    change = payment - total_to_pay
                    print(f"Payment successful! Your change is: ${change:.2f}")
                    break
                else:
                    print("Insufficient funds. Please pay the full amount.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    else:
        print("No items ordered. Have a nice day!")

if __name__ == "__main__":
    main()