import sys
import auth
import admin
import store_manager
import delivery_partner
import customer

def main():
    while True:
        print("\n" + "="*70)
        print("               AT DOORSTEP - QUICK COMMERCE PLATFORM")
        print("="*70)
        print(" [1] Existing User Login")
        print(" [2] New Customer Sign-Up")
        print(" [3] Exit Platform")
        print("-" * 70)

        choice = input(" Select an option [1-3]: ").strip()

        if choice == '1':
            username = input("\n Enter Username : ").strip()
            password = input(" Enter Password : ").strip()

            user = auth.authenticate_user(username, password)

            if user:
                print(f"\n[AUTH SUCCESS] Welcome, {user['username']}!")
                print(f" Verified Role : {user['role']}")

                role = user['role']
                if role == 'ADMIN':
                    admin.show_dashboard(user['user_id'])
                elif role == 'STORE_MANAGER':
                    store_manager.show_dashboard(user['user_id'])
                elif role == 'DELIVERY_PARTNER':
                    delivery_partner.show_dashboard(user['user_id'])
                elif role == 'CUSTOMER':
                    customer.show_dashboard(user['user_id'])
            else:
                print("\n[AUTH FAILED] Invalid credentials or inactive account.")

        elif choice == '2':
            auth.register_customer()

        elif choice == '3':
            print("\nThank you for using At Doorstep! Goodbye.")
            sys.exit()

        else:
            print("\n[INVALID] Please select a valid option (1, 2, or 3).")

if __name__ == "__main__":
    main()