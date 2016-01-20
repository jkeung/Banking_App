__author__ = 'jkeung'
from Checking import Checking
from Savings import Savings
from Customer import Customer
from Bank import Bank
from util import DataValidation
import pickle
import os



class Menu(object):
    """Menu class represents the banking application's menu

    Attributes:
        bank (Bank): The bank
        exit (boolean): An indicator for an exit condition of when to leave the app

    """

    def __init__(self):
        """Constructor for the menu class

        Args:
            None

        """
        if not os.path.abspath('data/bank.pkl'):
            self.bank = pickle.load(open(os.path.abspath('data/bank.pkl')), 'r')
        else:
            self.bank = Bank()
        self.exit = False

    @staticmethod
    def print_header():
        """Function to print the menu's header

        Args:
            None

        """
        print("****************************************************************************")
        print("***********                                            *********************")
        print("***********  Welcome to Jason's Awesome Banking App!!  *********************")
        print("***********                                            *********************")
        print("****************************************************************************")
        print("")

    @staticmethod
    def print_menu():
        """Function to print the menu's options

        Args:
            None

        """
        print("Please make a selection ")
        print("1. Create a new account")
        print("2. Make a deposit")
        print("3. Make a withdrawal")
        print("4. Show account details")
        print("0. Exit")
        print("")

    def create_account(self):
        """Function to create an account in the bank

        Args:
            None

        """
        account_type = DataValidation.check_valid_account_type("Would you like a checking or savings account? ")
        if not account_type:
            return None
        first_name = DataValidation.check_valid_name("What is your first name? ")
        if not first_name:
            return None
        last_name = DataValidation.check_valid_name("What is your last name? ")
        if not last_name:
            return None
        ssn = DataValidation.check_valid_ssn("What is your social security number? ")
        if not ssn:
            return None
        initial_deposit = DataValidation.get_valid_initial_deposit(account_type, "What is your initial deposit? ")
        if not initial_deposit:
            return None

        if account_type == "Checking":
            account = Checking(initial_deposit)
        elif account_type == "Savings":
            account = Savings(initial_deposit)

        customer = Customer(first_name, last_name, ssn, account)
        self.bank.add_customer(customer)

    def make_deposit(self):
        """Function to make a deposit into a customer's account

        Args:
            None

        """
        customer = self.bank.select_customer()

        if not customer:
            return None

        account = customer.account
        print("You currently have a balance of {0:.2f}".format(account.balance))
        amount = DataValidation.check_positive_float("How much would you like to deposit? ")

        if amount == 0:
            return None

        account.deposit(amount)

        return None

    def make_withdrawal(self):
        """Function to withdraw money from an account in the bank

        Args:
            None

        """
        customer = self.bank.select_customer()

        if not customer:
            return None

        proceed = DataValidation.check_valid_yes_no("Withdrawals incur a $5.00 fee, would you like to proceed? (Y/N) ")

        if not proceed:
            return None

        account = customer.account
        print("You currently have a balance of {0:.2f}".format(account.balance))
        amount = DataValidation.check_positive_float("How much would you like to withdraw? ")

        if amount == 0:
            return None

        account.withdraw(amount)

        return None

    def show_details(self):
        """Function to create an account in the bank

        Args:
            None

        """
        customer = self.bank.select_customer()

        if not customer:
            return None

        print(customer)
        raw_input("Press enter key to continue...")
        print("")
        print("")

        return None

    def exit_menu(self):
        """Function to exit the menu and application

        Args:
            None

        """
        print("Thank you for visiting, see you next time!")
        self.exit = True

    def perform_action(self):
        """Function to perform an action from a menu's selection

        Args:
            None

        """
        if self.choice == 1:
            return self.create_account()
        elif self.choice == 2:
            return self.make_deposit()
        elif self.choice == 3:
            return self.make_withdrawal()
        elif self.choice == 4:
            return self.show_details()
        elif self.choice == 0:
            return self.exit_menu()

    def get_choice(self):
        """Function to get a valid choice from the menu

        Args:
            None

        """
        choice = -1

        while choice < 0 or choice > 4:

            try:
                choice = int(raw_input('Enter your selection please: '))
                print("")

                if choice < 0 or choice > 4:
                    print("Please select a valid choice between 0 and 4")

            except ValueError:
                print("Please input a valid selection, numbers only.")

        return choice

    def load_state(self):
        """Function to load the current state of the bank

        Args:
            None

        """
        return pickle.load(open(os.path.abspath('data/bank.pkl'), 'r'))


    def save_state(self):
        """Function to save the current state of the bank

        Args:
            None

        """
        pickle.dump(self.bank, os.path.abspath('data/bank.pkl'))

    def run_menu(self):
        """Function to run the menu

        Args:
            None

        """
        self.print_header()
        while not self.exit:
            self.print_menu()
            self.choice = self.get_choice()
            self.perform_action()

    def run(self):
        self.run_menu()
