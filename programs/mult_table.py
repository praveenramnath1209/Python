#Multiplication table 
table_num = int(input("enter the table no :"))
r = int(input("enter rage :"))
for i in range(1,r+1):
    print(f"{table_num} * {i}:" ,table_num*i)