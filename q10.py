# Wap to check whether the given integer is multiple of 3

n = int(input("Please enter an integer: "))
c = int(input("Please enter a choice: "))

if c == 1:
    # Approach 1: Using a simple if-else statement
    if n % 3 == 0:
        print("divisible by 3")
    else:
        print("not divisible by 3")
if c == 2:
    # Approach 2: Using a function
    def mul(n):
        return n % 3 == 0
    print(mul(n))
if c == 3:
    # Approach 3: Using a ternary operator
    print("divisible by 3" if n % 3 == 0 else "not divisible by 3")
if c == 4:
    # Approach 4: Using a lambda function
    is_multiple = lambda x: x % 3 == 0
    print(is_multiple(n))