arr = [5, 12, 8, 20, 3, 15]
target = 10

count = 0

for i in arr:
    if i > target:
        count+= 1

print(count)