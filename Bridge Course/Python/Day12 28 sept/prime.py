# 
# #checking for prime number
# num = int(input("Enter your number:\n"))
# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")

#prime number 
num=int(input("enter a num"))
flag=0
for i in range(2,(num//2)+1):
    if(num%i==0):
        flag=1
        break 
if flag==1:
    print("not prime")  
else:
    print("prime")
