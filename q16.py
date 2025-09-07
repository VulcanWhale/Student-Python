# Wap to check whether the given data is mutable or immutable.
import ast

print(f"'{a}' is of {type(a)} type of data, which is mutable"if type((a := ast.literal_eval(input("Please enter a value: ")))) in [list,set,dict] else f"'{a}' is of {type(a)} type of data, which is immutable", "\n",f"deallocation in progress (prints None when completed): {(a := None)}")