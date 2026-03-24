# 29. Wap to login into the Instagram with valid username and password. (enter password only if the user name is valid)
uname = "Anik"
pas = "Anik@123"

    
while True:
    if uname == (u := input("Please enter the username: ")):
        p = input("Please enter the password: ")
        if p == pas:
            print("login successfull")
            break
        else:
            print("please enter the correct password.")
    else:
        print("please enter the correct username.")

