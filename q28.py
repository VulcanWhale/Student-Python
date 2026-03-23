# Wap to print ‘Fizz’ if the given number is multiple of three print ‘buzz’ if the given number is multiple of 5 and print ‘Fizzbuzz’ if the number is multiple of both 3 and 5.

def fb():
    # 1. Get and validate the integer input
    while True:
        n = input("Please enter an integer: ")
        try:
            n = int(n)
            break
        except ValueError:
            print("please enter an integer only.")

    # 2. Let the user choose the approach
    while True:
        print("\nChoose an approach:")
        print("1. One-liner (Nested Ternary)")
        print("2. Match-Case (Modern Python)")
        choice = input("Enter 1 or 2: ")

        if choice == '1':
            print("\nResult (One-liner):")
            print("Fizzbuzz" if n % 3 == 0 and n % 5 == 0 else "Fizz" if n % 3 == 0 else "Buzz" if n % 5 == 0 else "no is not divisible by 3 nither by 5")
            break
        elif choice == '2':
            print("\nResult (Match-Case):")
            match (n % 3 == 0, n % 5 == 0):
                case (True, True):
                    print("Fizzbuzz")
                case (True, False):
                    print("Fizz")
                case (False, True):
                    print("Buzz")
                case _:
                    print("no is not divisible by 3 nither by 5")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

fb()
