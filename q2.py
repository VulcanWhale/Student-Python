# Wap to check whether the character is vowel or not.

c = input("Please enter a character: ")

if len(c) == 1:
    if c in 'aeiouAEIOU':
        print(f"'{c}' is a vowel.")
    else:
        print(f"'{c}' is a consonant.")
elif len(c) == 0:
    print("You have to enter at least one character.")
else:
    print("Please enter only one character.")
