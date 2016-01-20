from __future__ import absolute_import
from banking.Account import Account


class Savings(Account):
    """Savings class represents a customer's Savings bank account. Savings account accrue an interest of 5%
       if a customer has more than $10,000 in their account, otherwise they only get 2% interest.

    Attributes:
        account_type (string): The account type
        account_number (int): The customer's account number
        balance (float): The amount of money that is in an account
        interest_rate (float): The interest rate that a customer will receive

    """
    account_type = "Savings"

    def __init__(self, initial_deposit, account_number):
        """Constructor for the Savings Class

        Args:
        initial_deposit (float): The initial deposit that will be added to the account
        """
        super(Savings, self).__init__(initial_deposit, account_number)
        self._update_interest()

    def _update_interest(self):
        """Function to update the interest in the account based on how much money is currently in the account. If a
           customer has over $10,000 they will receive 5% interested, otherwise only 2% interest.

        Args:
            None
        """
        if self.balance > 10000:
            self.interest_rate = 0.05
        elif self.balance <= 10000:
            self.interest_rate = 0.02

    def __repr__(self):
        """Representation of Savings class object

        Args:
            None
        """
        output = ""
        output += "Account Type: {0}\n".format(self.account_type)
        output += "Account Number: {0}\n".format(self.account_number)
        output += "Balance: {0:.2f}\n".format(self.balance)
        output += "Interest Rate: {0}%\n".format(self.interest_rate*100)
        return output
