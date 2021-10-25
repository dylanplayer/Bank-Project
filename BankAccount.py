class BankAccount:
    def __init__ (self, full_name, account_number, balance) :
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance
    
    def deposit (self, amount) :
        self.balance += amount
        print(f'{self.full_name} deposited: ${amount} new balance: ${self.balance}')
    
    def withdraw (self, amount):
        if amount >= self.balance :
            print('Insufficient funds.')
            self.balance -= 10
            print(f'{self.full_name} charged overdraft fee of $10 new balance: ${self.balance}')
        else :
            self.balance -= amount
            print(f'{self.full_name} withdrew: ${amount} new balance: ${self.balance}')

    def get_balance (self) :
        print(f'{self.account_number} : {self.full_name}\'s current balance is {self.balance}')
        return self.balance
    
    def add_intrest (self) :
        self.balance += self.balance * 0.00083

    def print_statement (self) :
        print('\n***** Statement *****')
        print(self.full_name)
        print(f'Account No.: {self.account_number}')
        print(f'Balance: ${self.balance}')
        print('*********************\n')
