# Wap to check whether the given integer is 3 Digit number

a = int(input("Please enter a number: "))

# 1st approach
if 100<=a<=999:
    print(f"{a} is a three digit no.")
else:
    print(f"{a} is not a three digit no.")
