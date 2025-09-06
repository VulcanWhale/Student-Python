# Wap to check whether the given character is special or not.
import re
import string

choice = input("Enter a choice (1, 2, 3, or 4): ")

match choice:
    case '1':
        print(f"'{c}' is a special character" if len((c:= input("Please enter a character: "))) == 1 and not ('A'<= c <= 'Z' or 'a'<= c <= 'z' or '0'<= c <= '9') else f"'{c}' is not a special character")
    case '2':
        print(f"'{c}' is a special character" if len((c := input("Please enter a character: "))) == 1 and not c.isalnum() else f"'{c}' is not a special character")
    case '3':
        print(f"'{c}' is a special character" if len((c := input("Please enter a character: "))) == 1 and not re.match('^[a-zA-Z0-9]$', c) else f"'{c}' is not a special character")
    case '4':
        print(f"'{c}' is a special character" if len((c := input("Please enter a character: "))) == 1 and c not in string.ascii_letters and c not in string.digits else f"'{c}' is not a special character")
    case _:
        print("Invalid choice.")
