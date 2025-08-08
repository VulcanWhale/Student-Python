# Wap to check whether the data is single value data.

n = eval(input("Please enter some data: "))

if type(n) in [int, float, complex, bool]:
    print("Single value")
else:
    print("Multivalued data type")
