# Wap to check whether 2 values are pointing to the same memory or not.
import ast
#print(True if (a := ast.literal_eval(input("Enter  some value: "))) is (b := ast.literal_eval(input("Enter  some value: "))) else False)

print(True if id(a := ast.literal_eval(input("Enter  some value: "))) == id(b := ast.literal_eval(input("Enter  some value: "))) else False)