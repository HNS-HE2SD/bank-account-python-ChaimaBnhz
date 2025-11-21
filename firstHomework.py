from datetime import datetime

class Client:
    def __init__(self, cin, firstName, lastName, tel=""):
        self.__CIN = cin
        self.__firstName = firstName
        self.__lastName = lastName
        self.__tel = tel
        self.accounts = [] 

    def get_CIN(self): 
        return self.__CIN
    def get_firstName(self):
        return self.__firstName
    def get_lastName(self): 
        return self.__lastName
    def get_tel(self): 
        return self.__tel
    def set_tel(self, tel):
        self.__tel = tel

    def display(self):
        print(f"CIN: {self.__CIN}, Name: {self.__firstName} {self.__lastName}, Tel: {self.__tel}")

    def add_account(self, account):
        self.accounts.append(account)

    def list_accounts(self):
        print(f"Accounts for {self.__firstName} {self.__lastName}:")
        for a in self.accounts:
            print(f"Account {a.get_code()}, Balance: {a.get_balance()} DA")


class Account:
    __nbAccounts = 0

    def __init__(self, owner):
        Account.__nbAccounts += 1
        self.__code = Account.__nbAccounts
        self.__balance = 0.0
        self.__owner = owner
        self.transaction = []

    def get_code(self):
        return self.__code
    def get_balance(self):
        return self.__balance
    def get_owner(self):
        return self.__owner

    def credit(self, amount, account=None):
        if amount == 0: 
            raise ValueError("the amount you just entred is null!")
        if amount < 0:
            raise ValueError("Amount must be positive!")
        if account is None:
            self.__balance += amount
            t = Transaction(amount, "credit")
            self.transaction.append(t)
        else:
            if self.__balance < amount:
                raise ValueError("Insufficient balance for transfer!")
            
            self.__balance -= amount
            account.__balance += amount 
            t = Transaction(amount, "transfer")
            self.transaction.append(t)
            t2 = Transaction(amount, "transfer received")
            account.transaction.append(t2)

        choice = input("Do you want to show transaction history? (y/n): ").lower()
        if choice == "y":
            Transaction.displayTransactions(self.transaction)
        else:
            print("Thank you for choosing our service!")

    def debit(self, amount, account=None):
        if amount == 0:
            raise ValueError("the amount you just entred is null !")
        if amount < 0:
            raise ValueError("Amount must be positive!")
        if self.__balance >= amount:
            self.__balance -= amount
            t = Transaction(amount, "debit")
            self.transaction.append(t)
            if account is not None:
                account.credit(amount)
            choice = input("Do you want to show transaction history? (y/n): ").lower()
            if choice == "y":
                Transaction.displayTransactions(self.transaction)
            else:
                print("Thank you for choosing our service!")
        else:
            raise ValueError("Insufficient balance.")

    def display(self):
        print(f"Account Code: {self.__code}")
        print(f"Owner: {self.__owner.get_firstName()} {self.__owner.get_lastName()}")
        print(f"Balance: {self.__balance} DA")

    @staticmethod
    def displayNbAccounts():
        print("Total accounts created:", Account.__nbAccounts)


class Transaction:
    __nbTransaction = 0

    def __init__(self, amount, typeTransaction):
        Transaction.__nbTransaction += 1
        self.__number = Transaction.__nbTransaction
        self.__amount = amount
        self.__typeTransaction = typeTransaction
        now = datetime.now()
        self.date = now.date()
        self.time = now.strftime("%H:%M:%S")

    @staticmethod
    def displayTransactions(transactions_list):
        print("_"*80)
        print(f"|{'number':<6}|{'type of operation':15}|{'amount':<8}|{'date':<10}|{'time':<8}|")
        print("_"*80)
        for t in transactions_list:
            print(f"|{t._Transaction__number:<6}|{t._Transaction__typeTransaction:<15}|{t._Transaction__amount:<8}|{t.date:<10}|{t.time:<8}|")
        print("_"*80)
