def check(st):
    rev=st[::-1]
    print("The string", st)
    print("The reverse: ", rev)
    if (st==rev):
        return True
    else:
        return False

x = input("Enter a string: ")
if check(x):
    print("It is palindrome")
else:
    print("It is palindrome")
