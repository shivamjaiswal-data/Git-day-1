i = 0
while i < 10:
    print(i)
    i += 1


# creating a table of 2 
i = int(input("Enter a number to print its table: "))
while i <= 10:
    print(f"{i} x 2 = {i * 2}")
    i += 1  

# Bug in Programm
I = [1, 2, 3, 4, 5,]
for n in I:
    print(n)
# continue statement
i = 0 
while i < 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1
    