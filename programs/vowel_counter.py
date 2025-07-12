def count_vow(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    text = text.lower()
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

st = input("Enter a text: ")
co = count_vow(st)
print("The number of vowels in the given string is:", co)
