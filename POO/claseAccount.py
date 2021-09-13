class Account:
    def __init__(self, name, account_number, initial_amount) -> None:
        self.name = name
        self.no = account_number
        self.balance = initial_amount

    def deposit(self,amount):
        self.balance = self.balance+ amount
    
    def withdraw(self,amount):
        if(self.balance-amount>=0):
            self.balance = self.balance - amount
        else:
            print('Sin saldo suficiente')

    def dump(self):
        s = '%s, %s balance %s ' %(self.name, self.no, self.balance)
        print(s)
