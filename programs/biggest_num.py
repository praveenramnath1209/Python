a = int(input("Enter number A:"))
b = int(input("Enter number B:"))
c = int(input("Enter number C:"))

if a>b & a>c:
    print("A is biggest among the three numbers ")
elif b>a & b>c:
    print("B is biggest among the three numbers ")
elif c>a & c>b:
    print("C is biggest among the three numbers ")
else:
    print("Invalid Input")