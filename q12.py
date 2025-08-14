# Wap to check whether the given character is digit or not.

n = input("Please enter a charecter: ")
c = int(input("Enter a choice (1,2 or 3):  "))

if len(n) == 1:
    if c == 1:
        if '0'<=n[0]<='9':
            print(f"'{n}' is a digit\n")
        else:
            print(f"'{n}' is not a digit\n")
    elif c == 2:
        if n.isdigit():
            print(f"'{n}' is a digit\n")
        else:
            print(f"'{n}' is not a digit\n")
    elif c == 3:
        print(f"'{n}' is a digit\n" if n.isdigit() else f"'{n}' is not a digit\n")
    else:
        print("Please enter a valid choice.. in between 1,2 or 3\n")
else:
    print("Please enter only one charecter, multiple charecters aren't allowed\n")