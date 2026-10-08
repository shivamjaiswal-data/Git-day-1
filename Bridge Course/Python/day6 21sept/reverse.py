# # we need to Reverse a given number
# num = int(input("Enter a number: "))
# rev = 0
# while num > 0:
#     dig  = num % 10
#     rev =rev * 10 + dig

#     num = num // 10
# print("Reversed number:", rev) 
#  we need palindrome number or not
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=x
        if x < 0:
            return False
        else:
              while num > 0:
                digit = num % 10
                reversed_num = reversed_num * 10 + digit
                n //= 10 
        return x == reversed_num