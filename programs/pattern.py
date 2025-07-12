n = int(input("Enter number of rows: "))

print("Select the option:")
print("(1) Left aligned")
print("(2) Right aligned")
an = int(input("Enter option (1 or 2): "))

# Left aligned
if an == 1:
    for i in range(1, n + 1):
        print("*" * i)

# Right aligned
elif an == 2:
    for j in range(1, n + 1):
        spaces = n - j
        print(" " * spaces + "*" * j)

else:
    print("Invalid input")
