arr = [3, 7, 2, 9, 5]

largest = arr[0]
second_largest = arr[0]

for i in arr:
    if i > largest:
     second_largest = largest
     largest = i


    elif i < largest and i > second_largest:
     second_largest = i
     
      
print(largest)
print(second_largest)