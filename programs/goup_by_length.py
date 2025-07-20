def wordlen(s):
    dc = {}
    s = s.lower().split()
    for i in s:
        l = len(i)
        if l in dc:
            dc[l].append(i)
        else:
            dc[l] = [i]
    return dc


inp = input("Enter a Text:")
x = wordlen(inp)
for lth, word in sorted(x.items(), reverse=True):
    print(f"{lth}: {word}")