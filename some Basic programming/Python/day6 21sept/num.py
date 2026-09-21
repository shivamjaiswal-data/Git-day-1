# we need to find the count of total number of digits in a given number
op = int(input("Enter a number: "))
count = 0
while  op > 0:
    op = op // 10
    count += 1
print("Number of digits:", count)
