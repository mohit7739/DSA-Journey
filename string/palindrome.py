s = input("Enter something: ")

reverse = ""
original = s
length = len(s)

for i in range(length-1,-1,-1):
    reverse = reverse + s[i]
    
if original == reverse:
    print("plaindrome")
else:
    print("palindrome")

print(reverse)