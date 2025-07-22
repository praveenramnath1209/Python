class BankAccount:
    def __init__(self,s,a):
        self.s = s
        self.a = a
    def deposit(self,x):
        self.a+=x
        print(f"\nAmount of {x} is added to your account , Current balance {self.a}")

    def withdraw(self,am):
        if self.a>am:
            self.a -= am
            print(f"\nAmount of {am} is withdrawn successfully, current balance : {self.a}")

    def disp(self):
        print(f"Name : {self.s}\nBalance : {self.a}")


b = BankAccount("Shanks",10000)
b.deposit(1000)
b.withdraw(100)
b.disp()

b1 = BankAccount("Levi",300000)
b1.deposit(1000)
b1.withdraw(100)
b1.disp()