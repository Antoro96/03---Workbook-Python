line = input("Enter a string: ")

is_Palindrome = True

for i in range(0, len(line) // 2):
    if line[i] != line[len(line)-i-1]:
        is_Palindrome = False

if is_Palindrome:
    print("The string is palindrome")   
else:
    print("The string is not palindrome") 