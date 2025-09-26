# Wap to find the second greatest of 4 values

import ast

#print(sorted(l if type(l := ast.literal_eval(input("Please enter a list: "))) == list else list(l))[-2])

l = ast.literal_eval(input("please enter a list of integers or floats: "))

for i in l:
    if not (type(i) == int or type(i) == float):
        print("list contains values other than integer or float")
        break

else:
    print(sorted(l)[-2])
        