arr = [2, 4, 6, 8, 10]

prefix = []
total = 0

for num in arr:
    total += num
    prefix.append(total)

print(prefix)