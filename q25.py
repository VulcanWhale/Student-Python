import ast

def get_numeric_inputs():
    """
    Prompts the user for a specified quantity of numeric values, 
    validates the input, and returns a list of numbers.
    """
    numbers_list = []
    try:
        num_count = int(input("How many numeric values do you want to enter? "))
    except ValueError:
        print("Invalid count. Please enter an integer.")
        return [] # Return an empty list if the count is invalid

    for i in range(num_count):
        while True: # Using 'while True' is more conventional than 'while 1'
            try:
                user_input = input(f"Enter number {i+1}: ")
                evaluated_input = ast.literal_eval(user_input)
                
                if isinstance(evaluated_input, (int, float)):
                    numbers_list.append(evaluated_input)
                    break # Exit the while loop on valid input
                else:
                    print("Invalid type. Please enter a real number (int or float).")
            
            # Catch specific errors from literal_eval or other issues
            except (ValueError, SyntaxError, TypeError):
                print("Invalid format. Please enter a valid number (e.g., 123 or 45.6).")

    return numbers_list

# --- How to use it ---
all_numbers = get_numeric_inputs()

if all_numbers:
    print("\nYou entered the following numbers:", all_numbers)
    print("The minimum value is:", min(all_numbers))