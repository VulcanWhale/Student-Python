# 30. Wap to print the middle value of a list only if it is string.
import ast

try:
    l = ast.literal_eval(input("please enter a list: "))
except (ValueError, SyntaxError):
    print("Invalid input format. Please enter a proper list like ['a', 'b', 'c'].")
    exit()

if isinstance(l, list):
    if len(l) % 2 == 0:
        print("this list has no middle value")
    else:
        # Check if middle element is a string
        m = l[len(l) // 2]
        if isinstance(m, str):
            print(f"the middle value is : {m}")
        else:
            print("middle value isn't a string")
        del m
else:
    print("please enter a list only")

del l