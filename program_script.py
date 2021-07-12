from subpackage import account

jose = account.Account('jose',500)

jose.deposit(800)
jose.deposit(2200)
jose.withdraw(500)
jose.withdraw(8000)

str(jose)


del jose