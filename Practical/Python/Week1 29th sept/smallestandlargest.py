num = int(input("Enter How many numbers you write in the List :\n"))
lst =[]
for  i in range (num):
    n = int(input("Enter the numbers:"))
    lst.append(n)
largest =lst[0]
second_lrgst=lst
for i in lst:
    if i > largest:
        largest = i

print(largest)

