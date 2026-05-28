s = "education"
s = s.lower()

count = 0
for c in s:
    if c in "aeiou":
        count = count + 1
print(count)