num = int(input("Enter a positive integer: "))

result = ""
q = num

r = q % 2
result = str(r) + result
q = q // 2

while q>0:
    r = q % 2
    result = str(q) + result
    q = q // 2

    print(num, "in Decimal is", result, "in Binary") 
    
