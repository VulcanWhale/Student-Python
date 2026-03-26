# 31. Wap to check whether the character is vowel or consonant.

def boundary_range_approach():
    print("\n--- Running Boundary Range Approach ---")
    n = input("please enter a character: ").lower()
    if len(n) == 1:
        if n in 'aeiou':
            print("vowel")
        elif ('a' <= n <= 'z') and n not in 'aeiou':
            print("Consonant")
        else:
            print("not an alphabet")
    else:
        print("enter only a single character.")
    
    del n

def one_liner_approach():
    print("\n--- Running One-Liner Approach ---")
    print("please enter a single character" if len(n := input("please enter a character: ").lower()) != 1 else "vowel" if n in "aeiou" else "consonant" if ('a' <= n <= 'z') else "not an alphabet")

    del n

if __name__ == "__main__":
    while True:
        print("\nChoose an approach:")
        print("1. Boundary Range (Manual)")
        print("2. One-Liner (Compact)")
        print("q. Quit")
        choice = input("Enter 1, 2 or q: ")

        if choice == '1':
            boundary_range_approach()
            del choice
        elif choice == '2':
            one_liner_approach()
            del choice
        elif choice.lower() == 'q':
            del choice
            break
        else:
            print("Invalid choice. Please enter 1, 2 or q.")
            del choice
