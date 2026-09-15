#Display numbers from -10 to -1
i = -10
while i < 0:
    print(i)
    i = i+1

# Calculate the sum of all natural number 1 to n in a given List 
lst = [1, 2, 3, 4, 5, 8, 9, 10 ] 
i = 0
sum = 0
while i < len(lst):
    sum = sum + lst[i]
    i = i + 1 
print("The sum of all natural number in the list is: ", sum)


#Calculate the sum of all natural number 1 to n in a given List 
lst = [1, 2, 3, 4, 5, 8, 9, 10 ] 
i = 0
sum = 0
while i < len(lst):
    sum = sum + lst[i]
    i = i + 1 
print("The sum of all natural number in the list is: ", sum/len(lst))

