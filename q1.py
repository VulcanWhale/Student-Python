# 1. Wap to print the square of a number only if it is even.

n = eval(input("Please enter a number: "))

if isinstance(n,int):
    if n % 2 == 0:
        print(f"the square of {n} is {n*n}")
    else:
        print(f"{n} is an odd number, so we aren't printing any square.")
else:
    print("Please enter an integer only.")