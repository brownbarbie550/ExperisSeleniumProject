class Bank_Account:
    # Attributes: name, account_num, balance, transactions, credit_limit
    # Methods: Deposit, Withdraw, Print Details
    def __init__(self, name, account_num, balance = 0):
        self.name = name
        self.account_num = account_num
        self.balance = balance
        self.transactions = []
        self.credit_limit = -2000

    def print_details(self):
        """print the account details"""
        print(f"name:{self.name} number:{self.account_num} balance:{self.balance}\n"
              f"{self.transactions}")

    def deposit(self, money):
        """a method that receives amount of money and add it to the balance
        and to the transaction list"""
        self.balance += money
        self.transactions.append(money)

    def withdraw(self, money):
        """a method that receives amount of money and subtract it from the balance
        (according to the credit limit)and add it to the transaction list"""
        if self.balance - money >= self.credit_limit:
            self.balance -= money
            self.transactions.append(-money)
        else:
            print(f"the balance is {self.balance}, there isn't enough money to withdraw")

    def overdraft(self):
        """the method returns if the account is overdraft or not"""
        # return self.balance < 0: #another option to write the code
        if self.balance < 0:
            return True
        else:
            return False




if __name__ == "__main__":

    my_account = Bank_Account("Avi", 1234, 150)
    print(my_account.name)
    my_account.print_details()

    my_account.deposit(500)
    my_account.print_details()

    name = input("enter name: ")
    acc_num = int(input("enter account number: "))
    your_account = Bank_Account(name, acc_num)
    your_account.print_details()

    """we can access the (self)s anytime and update them this way to the relevant object"""
    your_account.credit_limit = -3000

    amount = int(input("enter how much money to deposit: "))
    your_account.deposit(amount)
    your_account.print_details()

    amount = int(input("enter how much money to withdraw: "))
    your_account.withdraw(amount)
    your_account.print_details()

    amount = int(input("enter how much money to withdraw: "))
    your_account.withdraw(amount)
    your_account.print_details()

    #if the account is in overdraft - deposit 200 to the account
    if your_account.overdraft():
        print("ypu are in overdraft - let's help you a little with 200 extra....")
        your_account.deposit(200)
    else:
        print("you are a good client")

    your_account.print_details()