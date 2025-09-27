# 26. Wap to check the relation between two integer numbers.

def check():
    while True:
        # using infinite loop so that untill the user enters the correct input, it will continue to take the inputs
        try:
             # taking the inputs and comparing the two values
             print("the numbers are equal" if (a:= int(input("Please enter an integer: ")))==(b := int(input("Please enter the 2nd integer value: "))) else f"{a} is greater than {b}" if a>b else f"{a} is less than {b}")

             break      # coming out of the loop as my work is done
        except ValueError:
            # handling the specific value error exception
            print("Please enter an integer only.....(12,23,-45,etc.)")


# final working of the functional program
check()