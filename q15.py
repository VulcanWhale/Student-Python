# Wap to check whether the number is even or odd.

choice =  int(input("Please enter a choice (1 or 2): "))

match choice:
    case 1:
        print(f"{a} is an even number" if (a := int(input("Please enter a number: "))) & 1 == 0 else f"{a} is an odd number")
        a = None
        print(a)
    case 2:
        print(f"{a} is an even number" if (a := int(input("Please enter a number: ")))%2 != 1 else f"{a} is an odd number")
        del a
    case _:
        print("Invalid Choice!")