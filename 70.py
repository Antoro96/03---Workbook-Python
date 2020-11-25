message = input("Enter a message: ")
amount = int(input("Enter the shifted amount: "))

new_message = ""
for ch in message:
    if ch >= "a" and ch <= "z":
        pos = ord(ch) - ord("a")
        pos = (pos + amount) % 26
        new_char = chr(pos + ord("a"))
        new_message = new_message + new_char
    elif ch >="A" and ch <="Z":
        pos = ord(ch) - ord("A")
        pos = (pos + amount) % 26
        new_char = chr(pos + ord("a"))
        new_message = new_message + new_char
    else:
        new_message = new_message + ch
    
print("The shifted message is", new_message)


