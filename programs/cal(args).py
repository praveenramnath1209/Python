def cal(*args, n):
    if n == 1:
        total = 0
        for i in args:
            total += i
    elif n == 2:
        total = args[0]
        for j in args[1:]:
            total -= j
    elif n == 3:
        total = 1
        for k in args:
            total *= k
    else:
        return "Invalid operation"
    
    return total

print(cal(1, 6, 7, 3, 4, n=2)) 

