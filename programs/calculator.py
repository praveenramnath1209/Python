a = int(input("enter number a :"))
b = int(input("enter number b :"))

print("Choose operation")
print("1.ADD")
print("2.SUB")
print("3.MUL")
print("4.DIV")

n = int(input("Enter the option (1 to 4):"))

if n == 1:
    print(a+b)
elif n==2:
    print(a-b)
elif n==3:
    print(a*c)
elif n==4:
    if b != 0:
        print(a/b)
else:
    print("Invalid input")