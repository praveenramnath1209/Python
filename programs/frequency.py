def freq(s):
    dict_f= {}
    for f in s:
        if f in dict_f:
            dict_f[f] += 1
        elif f not in dict_f:
            dict_f[f]= 1
    return dict_f


inp = input('Enter a string :')
cc = freq(inp)
print("Frequency")
for k ,v in cc.items() :
    print(f"{k}:{v}")