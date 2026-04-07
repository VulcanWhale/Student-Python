# 33. Wap to print the value as it is only if the length of the value is even.

import ast

print(f"you have entered a {type(n)}" if isinstance((n := ast.literal_eval(input("Please enter a collection type data: "))),(str,list,tuple,set,dict))else "please enter a collection" if len(n)%2 == 0 else f"the {type(n)} is of odd length")
