arr = [1, 2, 3, 2, 4, 1]


length = len(arr)

for i in range(length):

    for j in range(i + 1, length):
      if arr[i] == arr[j]:
       print(arr[i])

