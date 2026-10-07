# list i want  to apply sum and count and sorting methods on list
my_list = [1, 2, 3, 4, 5]
print("Sum:", sum(my_list))
print("Count:", len(my_list))
my_list.sort()
print("Sorted:", my_list)
#and i want to apply descending order on list
my_list.sort(reverse=True)
print("Descending:", my_list)

#create a list of 10 numbers and Display the sum of laste four numbers in the list
numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
last_four_sum = sum(numbers[-4:])
print("Sum of last four numbers:", last_four_sum)
#remove the items from the list located at index 2 and 5 position
del numbers[2]
del numbers[5]
print("List after removing items at index 2 and 5:", numbers)   
#print the difference of highest and lowest number in the list
print("Difference between highest and lowest number:", max(numbers) - min(numbers))

#append a new element in the list which is half of the item of third position in the list
numbers.append(numbers[2] / 2)
print("List after appending half of the third item:", numbers)
