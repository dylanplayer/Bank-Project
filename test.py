from BankAccount import BankAccount

account_1 = BankAccount('John Doe', '3141589', 100.00)
account_1.deposit(50.00)
account_1.get_balance()
account_1.add_intrest()
account_1.print_statement()

account_2 = BankAccount('Jane Doe', '3141590', 100.00)
account_2.deposit(75.00)
account_2.get_balance()
account_2.add_intrest()
account_2.print_statement()

account_3 = BankAccount('Bill Doe', '3141591', 100.00)
account_3.deposit(100.00)
account_3.get_balance()
account_3.add_intrest()
account_3.print_statement()

account_4 = BankAccount('Michell', '3141592', 100.00)
account_4.deposit(400000)
account_4.print_statement()
account_4.add_intrest()
account_4.print_statement()
account_4.withdraw(150)
account_4.print_statement()
