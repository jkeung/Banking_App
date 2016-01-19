__author__ = 'jkeung'


class Account(object):
    """Account class represents a customer's bank account"""
    
    account_number = 1000000
    withdrawal_charge = 5

    def __init__(self, initial_deposit):
        self.balance = initial_deposit
        self.account_number = Account.account_number
        Account.account_number += 1

    def withdraw(self, amount):

        if amount + self.withdrawal_charge > self.balance:
            print ("Insufficient Funds")
            return None

        self.update_interest()

        self.balance -= amount + self.withdrawal_charge
        print("Successfully withdrew ${0:.2f} and incurred a fee of ${1:.2f}".format(amount, self.withdrawal_charge))
        print("Your new balance is ${0:.2f}".format(self.balance))
        print("")

    def deposit(self, amount):
        if amount < 0:
            print("Cannot deposit a negative amount")
            return None
        self.update_interest()
        self.balance += amount + amount * self.interest_rate
        print("Successfully deposited ${0:.2f} with an interest of {1:.2f}%".format(amount, self.interest_rate*100))
        print("Your new balance is ${0:.2f}".format(self.balance))
        print("")

    def update_interest(self):
        if self.balance > 10000:
            self.interest_rate = 0.05
        elif self.balance <= 10000:
            self.interest_rate = 0.02


