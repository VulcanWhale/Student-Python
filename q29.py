# 29. Wap to login into the Instagram with valid username and password. (enter password only if the user name is valid)
uname = "Anik"
pas = "Anik@123"

while True:
    if uname == input("Please enter the username: "):
        # Nested loop: Once username is correct, only ask for the password
        while True:
            p = input("Please enter the password: ")
            if p == pas:
                print("login successful")
                # Exit both loops
                break 
            else:
                print("please enter the correct password.")
        break # Exit the outer loop once the inner one breaks (after success)
    else:
        print("please enter the correct username.")
