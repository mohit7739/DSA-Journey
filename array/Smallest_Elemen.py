arr = [5, 2, 8, 1, 9]

smallest = arr[0]

for x in arr:
    if x < smallest:
        smallest = x

print(smallest)