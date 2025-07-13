def arm(num):
    sum = 0
    n = len(str(num))

    while num > 0:
        digit = num % 10
        sum = sum + digit ** n
        num = num //10
    
    return sum

number = int(input("Enter a number:"))
sum = arm(number)
print(sum)
if (number==sum):
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")