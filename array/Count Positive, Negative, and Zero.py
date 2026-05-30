arr = [3, -1, 0, 5, -2, 0]

count_pos = 0
count_neg = 0
count_zero =0

for i in arr:
    if i > 0:
        count_pos += 1
    elif i < 0:
        count_neg += 1
    else:
        count_zero += 1

print(count_zero)
print(count_neg)
print(count_pos)