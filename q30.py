# 30. Wap to print the middle value of a list only if it is string.
import ast

l = ast.literal_eval(input("please enter a list: "))

if len(l)%2 == 0:
    print("this list has no middle value")
else:
    if isinstance(l[len(l)//2],str):
        print(f"the middle value is : {l[len(l)//2]}")
    else:
        print("middle value isn't a string")