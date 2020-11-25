from random import randrange
print("Celsius Temperature", "\t", "Fahrenheit Temperature")
for currentCelsiusTemperature in range(101):
    FTempEquivalent = (currentCelsiusTemperature * 1.8) + 32
    print("\t", currentCelsiusTemperature,"\t\t\t", \
         format( FTempEquivalent,".1f"))

#C = (F - 32) / 1.8

#F = (C * 1.8) + 32

