PENNIES_PER_NICKEL = 5
NICKEL = 0.05

total = 0.00

line = input("Enter the price of the item: ")

while line != "":
    total = total + float(line)

    line = input("Enter the price of the item: ")

    print("The amount payble is %02f" % total)

    rounding_indicator = total * 100 % PENNIES_PER_NICKEL

    if rounding_indicator < PENNIES_PER_NICKEL /2:
        total_cash = total - rounding_indicator /100
    else:
        total_cash = total + NICKEL - rounding_indicator /100

    print("The cash amount payble is %02f" % total_cash)
