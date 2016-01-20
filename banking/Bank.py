#!/usr/bin/env python
from __future__ import absolute_import
from banking.Checking import Checking
from banking.Savings import Savings


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
        if not self.customers:
            print("You have no customers, please create some. \n")
            return None

        self._print_customer_list()

        selection = raw_input("Please select an account: ")
        if selection == "0":
            return None

        if not selection.isdigit():
            print("Please specify a number from the list of customers. \n")
            return self.select_customer()

        selection = int(selection)

        if selection not in range(len(self.customers)):
            print("Please specify a number from the list of customers. \n")
            return self.select_customer()

        return self.customers[selection-1]

    def add_account(self, initial_deposit, account_type):
        """Function to add an account to a bank

        Args:
            initial_deposit (float): The initial deposit needed to start an account
            account_type (string): Identifier of a checking or savings account

        """
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
