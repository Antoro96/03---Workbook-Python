n = int(input("Enter a positive number:"))
m = int(input("Enter a positive number: "))

d = min(n, m)

while n % d != 0 or m % d != 0:
    d = d - 1

print("The greatest common divisor of", n, "and", m, "is", d, ".")
