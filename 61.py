
list = []


n = int(input("Enter a value: "))
if n<=0:
      print("Error message!")
      exit()
while n != 0:
      list.append(n)
      n = int(input("Enter a value: "))

print("The values are: ")
for n in list:
      print(n)



            