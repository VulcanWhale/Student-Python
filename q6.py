# Wap to check whether the last digit of a given number is 5.

n = int(input("Please enter an integer: "))

if abs(n) % 10 == 5:
    print(f"{n} has 5 as the last digit.")
else:
    print(f"{n} doesn't have 5 as the last digit.")
