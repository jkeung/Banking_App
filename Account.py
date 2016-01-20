__author__ = 'jkeung'


class Account(object):
    """Account class represents a customer's bank account.

    Attributes:
        account_number (int): A unique identifier for a given account. This number starts at 1000000 and
                            increments every time a new account is created
        balance (float): The amount of money that is in an account
        interest_rate (float): The interest rate that a customer will receive
        withdrawal_charge (float): A fixed withdrawal_charge that is added to all withdrawals from an account


    """
    account_number = 1000000
    withdrawal_charge = 5.0

    def __init__(self, initial_deposit):
        """Constructor for the Account Class

        Args:
        initial_deposit (float): The initial deposit that will be added to the account
        """

        self.balance = initial_deposit
        self.account_number = Account.account_number
        self.interest_rate = 0.0
        Account.account_number += 1

    def withdraw(self, amount):
        """Function to withdraw money from an account. All withdrawals incur a fixed fee of $5.00

        Args:
            amount (float): The amount that will removed from the account.
        """
        # logic to check if customer is able to make withdrawal
        if amount + self.withdrawal_charge > self.balance:
            print ("Insufficient Funds")
            return None
        # update interest rates, and subtract withdrawal + fees
        self._update_interest()
        self.balance -= amount + self.withdrawal_charge
        print("Successfully withdrew ${0:.2f} and incurred a fee of ${1:.2f}".format(amount, self.withdrawal_charge))
        print("Your new balance is ${0:.2f}".format(self.balance))
        print("")

    def deposit(self, amount):
        """Function to deposit money from an account. In this bank, all deposits will receive a variable interest rate
           depending on how much money is in the account.

        Args:
            amount (float): The amount that will be added to the account.
        """
        # logic to check if customer is able to make deposit
        if amount < 0:
            print("Cannot deposit a negative amount")
            return None

        self._update_interest()
        self.balance += amount + amount * self.interest_rate
        print("Successfully deposited ${0:.2f} with an interest of {1:.2f}%".format(amount, self.interest_rate*100))
        print("Your new balance is ${0:.2f}".format(self.balance))
        print("")

    def _update_interest(self):
        """Function to update the interest in the account based on how much money is currently in the account.

        Args:
            None

        """
        pass
