__author__ = 'jkeung'


class Customer(object):
    """Customer class represents a single customer at a bank

    Attributes:
        first_name (string): The customer's first name
        last_name (string): The customer's last name
        ssn (string): The customer's social security number
        account (Account): The customer's account

    """

    def __init__(self, first_name, last_name, ssn, account):
        """Constructor for the Customer Class

        Args:
        first_name (string): The customer's first name
        last_name (string): The customer's last name
        ssn (string): The customer's social security number
        account (Account): The customer's account

        """
        self.first_name = first_name
        self.last_name = last_name
        self.ssn = ssn
        self.account = account

    def __repr__(self):
        """Representation of Customer class object

        Args:
            None

        """
        output = ""
        output += "Customer Information\n"
        output += "First Name: {0}\n".format(self.first_name)
        output += "Last Name: {0}\n".format(self.last_name)
        output += "SSN: {0}\n".format(self.ssn)
        output += "{0}".format(self.account)
        return output

    def display_info(self):
        """Function to display the key attributes of an account in a shortened format

        Args:
            None

        """
        output = ""
        output += "First Name:{0} Last Name:{1} SSN: {2} Account #:{3} Balance:{4:.2f}" \
            .format(self.first_name, self.last_name, self.ssn, self.account.account_number, self.account.balance)
        return output
