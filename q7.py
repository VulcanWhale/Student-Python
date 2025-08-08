# Wap to check whether the given data is float.
print("Program to check whether a given input is float or not. ")

n = eval(input("Please enter something: "))

if type(n) == float:
    print(f'{n} is a floating point number')
else:
    print(f"{n} isn't a float")
