# Consider a tuple of length 2 and check whether the tuple is homogenous or not.

import ast

def tup():
    while True:
        try:
            print(len(a:= ast.literal_eval(input("please enter a tuple: "))) == 2 and type(a) == tuple and type(a[0]) == type(a[1]))
            del a
            break
        except(ValueError,SyntaxError,TypeError,IndexError):
            print("Invalid input. Please enter a valid tuple literal, for example: (1, 2) and Input must be a tuple of length 2")

tup()