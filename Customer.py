__author__ = 'jkeung'


class Customer(object):

    def __init__(self, first_name, last_name, ssn, account):
        self.first_name = first_name
        self.last_name = last_name
        self.ssn = ssn
        self.account = account

    def __repr__(self):
        output = ""
        output += "Customer Information\n"
        output += "First Name: {0}\n".format(self.first_name)
        output += "Last Name: {0}\n".format(self.last_name)
        output += "SSN: {0}\n".format(self.ssn)
        output += "{0}".format(self.account)
        return output

    def display_info(self):
        output = ""
        output += "First Name:{0} Last Name:{1} SSN: {2} Account #:{3} Balance:{4:.2f}" \
            .format(self.first_name, self.last_name, self.ssn, self.account.account_number, self.account.balance)
        return output

    def get_account(self):
        return self.account
