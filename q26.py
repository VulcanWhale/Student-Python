# 26. Wap to check the relation between two integer numbers.

def check():
    while True:
        try:
             print("the numbers are equal" if (a:= int(input("Please enter an integer: ")))==(b := int(input("Please enter the 2nd integer value: "))) else f"{a} is greater than {b}" if a>b else f"{a} is less than {b}")
             break
        except ValueError:
            print("Please enter an integer only.....(12,23,-45,etc.)")

check()