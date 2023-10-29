class BankAccount:
    def _init_(self):
        self.balance = {"Ram":5000,"Priya":400}
        
        
    def deposit1(self,name,deposit):
        total = 0
        if self.balance[name]>=0:
            total += self.balance[name]+deposit
            print(total)
    def withdraw1(self,name,withdraw):
        total = 0
        if self.balance[name]>=0:
            total = self.balance[name]-withdraw
            print(total)



# amount = int(input("Enter the Amount"))
# account.deposit(amount)
# withdraw = int(input("Amount to withdrawn"))
# account.withdraw(withdraw)
# inputoption = int(input("Enter the Input"))

account = BankAccount()
while True:
    print("1. To Deposit")
    print("2. To Withdraw")
    print("3.exit")
    user_input = int(input("Enter the choice"))
    if user_input == 1:
        Name = input("Enter the Name: ")
        deposit = int(input("Enter the Input"))
        account.deposit1(Name,deposit)
    elif user_input == 2:
        Name = input("Enter the Name: ")
        withdraw = int(input("Enter the amount to Withdraw"))
        account.withdraw1(Name,withdraw)
    elif user_input == 3:
        exit()
    else:
        print("Incorrect Entry")