# 32. Wap to find the greatest of 4 numbers.
import ast
n = []

while len(n) < 4:
    try:
        # Combined: Walrus for assignment, Ternary for the 'else' message
        n.append(v) if isinstance(v := ast.literal_eval(input("Please enter an integer: ")), int) else print("Please enter an integer only")
    except (ValueError, SyntaxError):
        print("Invalid format! Please insert some integer (no special characters/letters).")

if n:
    print(f"The greatest number is: {max(n)}")
    del n
