from math import sqrt

perimeter = 0

first_x = float(input("Enter the x part of the coordinate: "))
first_y = float(input("Enter the y part of the coordinate: "))

prev_x = first_x
prev_y = first_y

line = input("Enter the x part of the coordinate (blank to the quit): ")
while line != "":
    x = float(line)
    y = float(input("Enter the y part of the coordinate: "))

    dist = sqrt((prev_x - x) ** 2 + (prev_y -y) ** 2)
    perimeter = perimeter + dist

    prev_x = x
    prev_y = y

    line = input("Enter the x part of the coordinate (blank to the quit): ")

dist = sqrt((prev_x - x) ** 2 + (prev_y -y) ** 2)
perimeter = perimeter + dist

#Result
print("The perimeter of the polygon is", perimeter)



    
