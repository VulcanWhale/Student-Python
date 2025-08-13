# Wap to check whether the data is mutable or not.

n = eval(input("Please enter some value: "))

c = input("Please enter a choice for which approach you wanna use (1, 2, or 3): ")

print("-" * 20)

if c == '1':
    print("Approach 1: Checking against a list of immutable types")
    # This approach assumes anything not in the list is mutable.
    # This may not be accurate for all types (e.g., frozenset).
    if type(n) not in [bool, int, float, complex, str, tuple]:
        print(f"The data '{n}' is considered MUTABLE.")
    else:
        print(f"The data '{n}' is considered IMMUTABLE.")

elif c == '2':
    print("Approach 2: Ternary operator checking for common mutable types")
    is_mutable = True if type(n) in [list, set, dict] else False
    if is_mutable:
        print(f"The data '{n}' is MUTABLE (list, set, or dict).")
    else:
        print(f"The data '{n}' is IMMUTABLE (or not a list, set, or dict).")

elif c == '3':
    print("Approach 3: Lambda function checking for common mutable types")
    is_mutable_func = lambda x: type(x) in [list, set, dict]
    if is_mutable_func(n):
        print(f"The data '{n}' is MUTABLE (list, set, or dict).")
    else:
        print(f"The data '{n}' is IMMUTABLE (or not a list, set, or dict).")

else:
    print("Invalid choice. Please enter 1, 2, or 3.")