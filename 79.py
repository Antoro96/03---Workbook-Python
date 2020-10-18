from random import randrange

NUM_ITEMS = 100

mx_value = randrange(1, NUM_ITEMS + 1)
print(mx_value)

num_updates = 0

for i in range(1, NUM_ITEMS):
    current = randrange(1, NUM_ITEMS + 1)

    if current < mx_value:
        mx_value = current
        num_updates = num_updates + 1
        print(current, "<==Update")
    else:
        print(current)

print("The maximum value is", mx_value)
print("The maximum value is updated", num_updates, "times.")
