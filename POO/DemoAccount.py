from claseAccount import Account

c1 = Account('Homero','001',20000)
c2 = Account('Marge','001',20000)
c1.deposit(1000)
c2.withdraw(4000)
c1.withdraw(4000)
c2.withdraw(10500)
c1.withdraw(3500)
print("c1 valance:",c1.balance)
c1.dump()
c2.dump()

