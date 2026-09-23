def sumofsqr(n):
    sum=0
    for i in range (1,n+1):
        sum = sum + i**2
    return sum
print(sumofsqr(6))