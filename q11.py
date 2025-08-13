# Wap to check whether the data is mutable or not.

n = eval(input("Please enter some value: "))

c = input("Please enter a choice for which approach you wanna use (1, 2, or 3): ")

print("-" * 20)

if c == '1':
    # Approach 1: Using if-else
    if type(n) not in [bool, int, float, complex, str, tuple]:
        print(f"'{n}' is a mutable data")
    else:
        print(f"'{n}' is an Immutable data")

elif c == '2':
    # Approach 2: Using ternary operator
    print(True if type(n) in [list,set,dict] else False)

elif c == '3':
    # Approach 3: Using lambda function
    is_mutable = lambda x: type(x) in [list, set, dict]
    print(is_mutable(n))

else:
    print("Invalid choice. Please enter 1, 2, or 3.")