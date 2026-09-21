# we need to Reverse a given number
op = int(input("Enter a number: "))
rev = 0
while op > 0:
    dig  = op % 10
    rev =rev * 10 + dig

    op = op // 10
print("Reversed number:", rev) 
