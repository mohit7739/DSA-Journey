arr = [5, 2, 8, 1, 9]

smallest = arr[0]
largest = arr[0]

for i in arr:
    if i > largest:
        largest = i
    elif i < smallest:
        smallest = i

print(smallest)
print(largest)