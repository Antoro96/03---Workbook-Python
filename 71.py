from math import sqrt

number = int(input("Enter a number: "))

guess =  number/2

if sqrt(number):
    if abs((guess * guess) - number) <= pow(10,-12):
        new_guess = abs((guess*guess)-number)
        print("The guess is good enough.", new_guess)
    else:
        guess = (guess + number/guess)/2
        print("The guess is not good enough.")
        print("The average is", guess)
else:
    print("The", number, "is not divisible")

    
    
