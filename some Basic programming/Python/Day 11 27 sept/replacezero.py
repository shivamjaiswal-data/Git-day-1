num = [0, 5, 0, 10, 0]
result = []
for i in num:
    if i != 0:
        result.append(i)
for i in num:
    if i == 0:
        result.append(i)
print(result)