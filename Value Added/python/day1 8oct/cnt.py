s = "hello"

arr = []

for x in s:
    count = s.count(x)

    if count > 1:
        arr.append(count)
    else:
        arr.append(0)

print(arr)