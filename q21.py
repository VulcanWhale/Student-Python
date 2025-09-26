# 21. Wap to check whether the char is uppercase, lowercase, digit or special char.

print("please enter only one charecter" if len(a := input("Please enter a charecter: ")) != 1 else "upper case" if a.isupper() else "Lower" if a.islower() else "digit" if a.isdigit() else "Special Charecter" )

del a