num = int(input("Enter a number : "))
if (num<=1):
    print(f"{num} is not a Prime Number")
else:
    is_p = True
    for i in range(2, num):
        if num % i == 0 :
            is_p = False
        break
    if is_p:
        print(f"{num} is Prime number ")
    else:
        print(f"{num} is not a Prime Number")