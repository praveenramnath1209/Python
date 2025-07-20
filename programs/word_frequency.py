def word_freq(s):
    wd = {}
    x = s.lower().split()
    for i in x:
        if i not in wd:
            wd[i] = 1
        elif i in wd:
            wd[i]+=1
    return wd


inp = input("Enter an Sentence :")
gg = word_freq(inp)
for k,v in gg.items():
    print(f"{k}:{v}")