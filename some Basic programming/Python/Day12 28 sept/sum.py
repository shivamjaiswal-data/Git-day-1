#sum of digit
# num = int(input("Enter a number:\n"))
# sum = 0
# while num > 0:
#     sum = sum + (num % 10)
#     num = num // 10
# print("Sum of digits:", sum)
# checking for palindrome number
num = int(input("Enter a number:\n"))
temp = num
reverse = 0
while num > 0:
    reverse = reverse * 10 + (num % 10)
    num = num // 10
if temp == reverse:
    print("Number is a palindrome")
else:
    print("Number is not a palindrome")