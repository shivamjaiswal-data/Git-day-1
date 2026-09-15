lst = [1, 2, 3, 4, 5, 8, 9, 10 ] 
i = 0
sum = 0
while i < len(lst):
    sum = sum + lst[i]
    i = i + 1 
print("The sum of all natural number in the list is: ", sum/len(lst))