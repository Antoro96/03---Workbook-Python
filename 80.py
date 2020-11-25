from random import randrange
import random
from random import randint

#faces = ["T", "H"]
flip = 10
heads = 0
tails = 0 
trials = 0
for i in range(flip):
    result = random.randint(0,1)
    trials +=1
    #print(result)
    if result == 0:
        heads += 1
        #print("Heads")
        
        #flip = heads
        #heads = heads + 1
        #print(faces, "(flips)")
    else:
        tails += 1
        #print("Tails")
        #faces = tails
        #tails = tails + 1
print(heads)

    








#print("On overage, 7.9 flips were needed")