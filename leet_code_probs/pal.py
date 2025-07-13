n = int(input("Enter a number:"))

s = str(n)

if s[0:]==s[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
