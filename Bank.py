__author__ = 'jkeung'
from Checking import Checking
from Savings import Savings

class Bank(object):
    """Bank class represents a single bank

    Attributes:
        customers (list): A list of a bank's customers

    """

    def __init__(self):
        """Constructor for the Bank Class

        Args:
            None

        """
        self.customers = []
        self.account_number_counter = 1000000

    def add_customer(self, customer):
        """Function to add a customer to a bank

        Args:
            customer (Customer): A bank's customer

        """
        self.customers.append(customer)

    def select_customer(self):
        """Function to select a customer from a bank

        Args:
            None

        """
        selection = -1

        if not self.customers:
            print("You have no customers, please create some. \n")
            return None

        while selection not in range(len(self.customers)):

            self._print_customer_list()
            # self._get_customer_selection()
            try:
                selection = int(raw_input("Please select an account: "))
                if selection == 0:
                    return None

                assert selection > 0
                return self.customers[selection-1]
            except (IndexError, AssertionError, ValueError):
                print("Please specify a number from the list of customers. \n")

        return None

    def add_account(self, initial_deposit, account_type):
        if account_type == "Checking":
            account = Checking(initial_deposit, self.account_number_counter)
        elif account_type == "Savings":
            account = Savings(initial_deposit, self.account_number_counter)
        self.account_number_counter += 1
        return account

    def _print_customer_list(self):
        """Function to print a list of customers

        Args:
            None

        """
        for i, customer in enumerate(self.customers):
            print("{0}. {1}".format(i+1, customer.display_info()))
        print("")

    def _get_customer_selection(self):
        """Function to select from a list of customers

        Args:
            None

        """
        try:
            selection = int(raw_input("Please select an account: "))
            if selection == 0:
                return None

            assert selection > 0
            return self.customers[selection-1]
        except (IndexError, AssertionError, ValueError):
            print("Please specify a number from the list of customers. \n")
