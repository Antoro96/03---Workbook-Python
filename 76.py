n = int(input("Enter an integer: "))

factor = 2

print("The prime factors of", n, "are:")
while n >= factor and n != 1:
    if n % factor == 0:
        n = n / factor
        print(factor)
    else:
        factor = factor + 1
        
            








