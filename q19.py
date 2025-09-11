#  Wap to check whether the string is palindrome or not

match (int(input("Please enter a choice(1 or 2): "))):
    case 1:
        print((a := input("Please enter a string: ")) == a[::-1])
        del a
    case 2:
        print((a := input("Please enter a string: ")) == "".join(reversed(a)))
        del a
    case _:
        print("Invalid choice!")