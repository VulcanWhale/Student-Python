# Wap to check whether the given character is digit or not.

n = input("Please enter a character: ")

if len(n) == 1:
    if n.isdigit():
        print(f"{n} is a digit")
    else:
        print(f"{n} is not a digit character")
else:
    print("Please enter a single character only, multiple characters aren't allowed")