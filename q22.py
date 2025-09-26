# 22. Wap to check whether the given integer is single digit or two digits or three digits or more than three digits.

print(f"{a} is a single digit integer" if 0<=abs(a :=  int(input("Please enter the value of a: ")))<=9 else f"{a} is a double digit integer" if 10<=abs(a)<=99 else f"{a} is a triple digit integer" if 100<=abs(a)<=999 else f"{a} has more than three digit.")