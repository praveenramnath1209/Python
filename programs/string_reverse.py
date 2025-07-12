def string_rev(str):
    s = str.replace(" ","").lower()
    print(s[::-1])



s = input("Enter text:")
string_rev(s)