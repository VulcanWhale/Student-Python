# Consider a character input if it is uppercase convert it into lowercase, if it is lowercase convert it into uppercase, if it is digit print the reminder when it is divided by 3 else if it is special character print it’s ASCII value.

def one_liner_approach():
    print("--- Running One-Liner Approach ---")
    a = input("Please enter a single character: ")
    if len(a) == 1:
        print(a.lower() if a.isupper() else a.upper() if a.islower() else str(int(a) % 3) if a.isdigit() else str(ord(a)))
    else:
        print("Please enter a single character. Multiple characters aren't allowed.")

def readable_approach():
    print("--- Running Readable If/Else Approach ---")
    char = input("Please enter a single character: ")
    if len(char) == 1:
        if char.isupper():
            print(char.lower())
        elif char.islower():
            print(char.upper())
        elif char.isdigit():
            print(int(char) % 3)
        else: # It must be a special character
            print(ord(char))
    else:
        print("Please enter a single character. Multiple characters aren't allowed.")

# --- Main Program ---
if __name__ == "__main__":
    choice = input("Which approach do you want to use?\n  1: One-Liner\n  2: Readable If/Else\nEnter choice: ")
    
    match choice:
        case '1':
            one_liner_approach()
        case '2':
            readable_approach()
        case _:
            print("Invalid choice. Please enter 1 or 2.")