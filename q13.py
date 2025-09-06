# Wap to check whether the given character is special or not.

c = input("PLease enter a charecter: ")
choice = input("Enter a choice (1 or 2): ")

match choice:
    case '1':
        print(f"'{c}' is a special charecter" if len(c) == 1 and not ('A'<= c <= 'Z' or 'a'<= c <= 'z' or '0'<= c <= '9') else f"'{c}' is not a special charecter")
    case '2':
        print(f"'{c}' is a special charecter" if len(c) == 1 and not c.isalnum() else f"'{c}' is not a special charecter")
    case _:
        print("Invalid choice.")