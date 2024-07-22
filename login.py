#Version 1:
#create an E-commerce project where the user can register and login himself using files in python.He 
#can see what all the products are present.The products contain Name ,Price ,category and Stock left.
#From these products user can place an order just by the product name and quantity he want tol purchase.
#Once he enters this a Bill should be generated with the total amount and a message written
#"Order has been placed!Complete the payment on the delivery."The change of stock should be reflected on the list of products
def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")

    print("Registration successful!")


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with open("users.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(",")
            if username == stored_username and password == stored_password:
                print("Login successful!")
                return True

    print("Invalid username or password.")
    return False


def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            if login():
                break
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
