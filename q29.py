# 29. Wap to login into the Instagram with valid username and password. (enter password only if the user name is valid)

def single_user_approach():
    print("\n--- Running Single-User Approach ---")
    uname = "Anik"
    pas = "Anik@123"

    while True:
        c = 0
        if uname == input("Please enter the username: "):
            while True:
                p = input("Please enter the password: ")
                if p == pas:
                    print("login successful")
                    del uname, pas, p, c # Cleanup variables before returning
                    return 
                else:
                    print("please enter the correct password.")
                    c += 1
                
                if c == 3:
                    print("maximum login attempts failed")
                    del uname, pas, p, c # Cleanup variables before returning
                    return 
        else:
            print("please enter the correct username.")

def multi_user_approach():
    print("\n--- Running Multi-User (Dictionary) Approach ---")
    users = {
        'Anik': 'Anik@123',
        'Hemanth': 'Hem@112',
        'Utkarsh': 'Utk1122',
        'Amber': 'dasAmber123'
    }

    while True:
        c = 0
        if (un := input("Please enter your username: ")) in users:
            while True:
                if (p := input("Please enter your password: ")) == users[un]:
                    print("login successful 😍")
                    del users, un, p, c # Cleanup variables before returning
                    return 
                else:
                    print("Please enter your password correctly")
                    c += 1
                
                if c == 3:
                    print("maximum login attempts failed")
                    del users, un, p, c # Cleanup variables before returning
                    return 
        else:
            print("Please enter your username correctly")

# Selection Menu
while True:
    print("\nChoose an approach for login:")
    print("1: Single-User")
    print("2: Multi-User (Dictionary Lookup)")
    choice = input("Enter 1 or 2 (or 'q' to quit): ")

    if choice == '1':
        single_user_approach()
        del choice
    elif choice == '2':
        multi_user_approach()
        del choice
    elif choice.lower() == 'q':
        del choice
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 'q'.")
        del choice
