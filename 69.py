import math

def main():
    '''
pi = 3 + 4/(2*3*4) + 4/(4*5*6) + 4/(6*7*8)...
'''
    
    sum = 0
    denom = 1
    sign = 1
    for i in range(15):
        sum = sum + 4 * sign/denom
        ##print(i, sign * denom, sum)
        denom = denom + 2
        sign = -sign

        print("The approx is", sum, "pi value is", math.pi)

main()


