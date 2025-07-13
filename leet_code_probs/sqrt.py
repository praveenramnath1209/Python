def sqr(n):
    if n > 0:
        val = int(n ** 0.5)
    return val

num = int(input("Enter the number :"))
print(sqr(num))