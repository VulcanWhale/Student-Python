# # Wap to check whether the given character is digit or not.
# 
# n = input("Please enter a character: ")
# 
# c = int(input("Please enter a choice for which approach you wanna use: "))
# 
# if c == 1:
#     if len(n) == 1:
#         if n.isdigit():
#             print(f"{n} is a digit")
#         else:
#             print(f"{n} is not a digit character")
#     else:
#         print("Please enter a single character only, multiple characters aren't allowed")
# elif c == 2:
#     if len(n) == 1:
#         if '0' <= n <= '9':
#             print(f"{n} is a digit")
#         else:
#             print(f"{n} is not a digit character")
#     else:
#         print("Please enter a single character only, multiple characters aren't allowed")
# 
# elif c == 3:
#     if len(n) == 1:
#         if n in '0123456789':
#            print(f"{n} is a digit")
#         else:
#            print(f"{n} is not a digit character")
#     else:
#        print("Please enter a single character only, multiple characters aren't allowed") 

# Refactored code starts here

# Wap to check whether the given character is digit or not.

n = input("Please enter a character: ")

if len(n) != 1:
    print("Please enter a single character only, multiple characters aren't allowed")
else:
    try:
        c = int(input("Please enter a choice for which approach you wanna use (1, 2, or 3): "))
    except ValueError:
        print("Invalid input for choice. Please enter a number.")
        exit()

    is_digit = False # Initialize to False

    if c == 1:
        is_digit = n.isdigit()
    elif c == 2:
        is_digit = '0' <= n <= '9'
    elif c == 3:
        is_digit = n in '0123456789'
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        exit()

    if is_digit:
        print(f"{n} is a digit")
    else:
        print(f"{n} is not a digit character")

# Refactored code ends here