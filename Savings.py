__author__ = 'jkeung'
from Account import Account


class Savings(Account):
    account_type = "Savings"

    def __init__(self, initial_deposit):
        super(Savings, self).__init__(initial_deposit)
        self.update_interest()

    def __repr__(self):
        output = ""
        output+="Account Type: {0}\n".format(self.account_type)
        output+="Account Number: {0}\n".format(self.account_number)
        output+="Balance: {0:.2f}\n".format(self.balance)
        output+="Interest Rate: {0}%\n".format(self.interest_rate*100)
        return output