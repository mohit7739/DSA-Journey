arr = [3, -1, 5, -2, -7, 4]

count_pos = 0
count_neg = 0

for i in arr:
    if i > 0:
        count_pos += 1
    elif i < 0:
        count_neg += 1

print(count_pos)
print(count_neg)