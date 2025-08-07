# Wap to print the cube of a number only if it is divisible by 9 or 6

a = int(input("Please enter a number: "))

if a % 9 == 0 or a % 6 == 0:
    print(a**3)
else:
    print(f"The number {a} is not divisible by 6 or 9.")