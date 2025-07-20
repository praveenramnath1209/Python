def vowc(st):
    freq = {}
    st = st.lower().replace(" ", "")
    vowels = 'aeiou'
    for ch in st:
        if ch in vowels:
            freq[ch] = freq.get(ch, 0) + 1
    return freq



inp = input("Enter the Text:")
x = vowc(inp)
print("Vowel frequency")
for vowel,freq in x.items():
    print(f"{vowel}:{freq}")

