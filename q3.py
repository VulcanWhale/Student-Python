# Wap to print Ascii value of a character only if it is upper case.

c = input("Please enter a character: ")

if len(c) == 1:
    if "A" <= c <= 'Z':
        print(f"The ASCII value of '{c}' is {ord(c)}")
    else:
        print(f"'{c}' is not an uppercase character.")
elif len(c) == 0:
    print("You have to enter at least one character.")
else:
    print("Please enter only one character.")
