# Wap to check whether the given integer is a 3-digit number

a = int(input("Please enter a number: "))

choice = input("Which approach do you want to use? (Enter 1 or 2):\n  1. Numeric Comparison\n  2. String Length Check\nYour choice: ")

print("-" * 20) # Separator for clarity

if choice == '1':
    print("Executing Approach 1: Numeric Comparison")
    # This approach works for positive numbers only.
    if 100 <= a <= 999:
        print(f"{a} is a three-digit number.")
    else:
        print(f"{a} is not a three-digit number.")
elif choice == '2':
    print("Executing Approach 2: String Length Check")
    # This approach also only works for positive numbers.
    if len(str(a)) == 3:
        print(f"{a} is a three-digit number.")
    else:
        print(f"{a} is not a three-digit number.")
else:
    print("Invalid choice. Please enter 1 or 2.")
