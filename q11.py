# Wap to check whether the data is mutable or not.

n = eval(input("Please enter some value: "))

if type(n) not in [bool,int,float,complex,str,tuple]:
    print(f"'{n}' is a mutable data")
else:
    print(f"'{n}' is an Immutable data")


print(True if type(n) in [list,set,dict] else False)

x = lambda n: type(n) in [list, set, dict]
print(x(n))