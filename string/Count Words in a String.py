s = "I love python"

space_count = 0
words = 0

for i in s:
    if i == " ":
     space_count +=1
words = space_count + 1

print(words)