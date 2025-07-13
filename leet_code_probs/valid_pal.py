def isPalindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

n = input("Enter a phrase:")
if(isPalindrome(n)):
    print("Valid Pal")
else:
    print("Not a valid pal")

    