class calc:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        if b!=0:
            return a/b


x = int(input("Enter number 1:"))
y = int(input("Enter number 2:"))

print("1.ADD\n2.SUB\n3.MULTIPLICATION\n4.DIVISION")
n = int(input("Select an option (1 to 4):"))
c = calc()

if n ==1:
    print(c.add(x,y))
elif n ==2:
    print(c.sub(x,y))
elif n==3:
    print(c.mul(x,y))
elif n==4:
    if y!=0:
        print(c.div(x,y))
    elif y==0:
        print("Division by Zero error")
