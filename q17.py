# Wap to check whether 2 values are pointing to the same memory or not.
import ast

c = int(input("please enter some choices(1 or 2): "))

match c:
    case 1:
        print((a := ast.literal_eval(input("Enter  some value: "))) is (b := ast.literal_eval(input("Enter  some value: "))))
        del a,b
    case 2:
        print(id(a := ast.literal_eval(input("Enter  some value: "))) == id(b := ast.literal_eval(input("Enter  some value: "))))
        del a,b
    case _:
        print("invalid choice")