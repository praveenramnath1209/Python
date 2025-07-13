def r_2_i(s):
    invalue = 0 
    s = s.upper().replace(" ","")
    dict = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}
    for i in range(len(s)):
        if i < len(s)-1 and dict[s[i]] < dict[s[i+1]]:
            invalue -=dict[s[i]]
        else:
            invalue += dict[s[i]]
    return invalue




s = input("Enter roman value :")
print(r_2_i(s))