#!/usr/bin/env python
from __future__ import absolute_import
from banking.Account import Account


class Checking(Account):
    """Checking class represents a customer's Checking bank account. Checking accounts do not accrue interest.

    Attributes:
        account_type (string): The account type
        account_number (int): The customer's account number
        balance (float): The amount of money that is in an account
        interest_rate (float): The interest rate that a customer will receive

    """
    account_type = "Checking"

    def __init__(self, initial_deposit, account_number):
        """Constructor for the Checking Class

        Args:
        initial_deposit (float): The initial deposit that will be added to the account

        """
        super(Checking, self).__init__(initial_deposit, account_number)
        self._update_interest()


    def _update_interest(self):
        """Function to update the interest in the account based on how much money is currently in the account. Checking
           accounts do not accrue interest.

        Args:
            None

        """
        self.interest_rate = 0

    def __repr__(self):
        """Representation of Checking class object

        Args:
            None

        """
        output = ""
        output+="Account Type: {0}\n".format(self.account_type)
        output+="Account Number: {0}\n".format(self.account_number)
        output+="Balance: {0:.2f}\n".format(self.balance)
        output+="Interest Rate: {0}%\n".format(self.interest_rate*100)
        return output
