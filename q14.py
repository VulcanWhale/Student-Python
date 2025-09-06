# Wap to check whether a list consists of middle value or not.

import ast

choice = int(input("Enter a choice (1, 2, or 3): "))

match choice:
    case 1:
        # if lenght of list is odd then middle value is there or else no middle value
        print("this list has a middle value " if len(l := ast.literal_eval(input("Please enter a list: "))) % 2 == 1 else "this list has no  middle value")
    case 2:
        # using bitwise operator if the last bit of the lenght is 1 i.e. the length is odd, then middle value is there or else it's not there
        print("this list has a middle value " if len(l := ast.literal_eval(input("Please enter a list: "))) & 1 else "this list has no  middle value")
    case 3:
        # mathematical way of checking 
        # formula (len(l)//2)*2 != len(l) 
        # e.g. (7//2)*2 != 7 ---> 3*2 != 7 -----> 6 != 7
        print("this list has a middle value " if (len((l := ast.literal_eval(input("Please enter a list: "))))//2)*2 != len(l) else "this list has no  middle value")
    case _:
        print("Invalid Choice.")
