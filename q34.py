# 34. Wap to print the last value of a list only if it is palindrome string starting with vowel.

'''
Goals for solving the problem:
1. Accept input from the user and safely evaluate it as a list.
2. Check if the inputted data is indeed a list.
3. Access the last element of the list.
4. Check if the last element is a string.
5. Check if the string starts with a vowel (a, e, i, o, u, case-insensitive).
6. Check if the string is a palindrome.
7. If all conditions are met, print the string.
'''

# Your code goes here:

import ast

l = ast.literal_eval(input("Please enter a list: "))

if isinstance(l,list):
    if isinstance(l[-1],str):
        if l[-1] == l[-1][::-1] and l[-1][0] in 'aeiouAEIOU':
            print(l[-1])
        else:
            print("the string isn't palindrome or it dosen't starts with a vowel")
    else:
        print("the last element isn't a string")
else:
    print(f"you haven't entered a list, it's a {type(l)}")


    

