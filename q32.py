# 32. Wap to find the greatest of 4 numbers.
import ast
n = []

while len(n) < 4:
    try:
        n += [v for v in [ast.literal_eval(input("Please enter an integer: "))] if isinstance(v, int)]
    except(ValueError,SyntaxError):
        print("currently the program can only accept integers only, please insert some integer")

print(max(n))
del n

