__author__ = 'jkeung'
from Checking import Checking
from Savings import Savings
from Customer import Customer
from Bank import Bank
from MixIns import HelperFunctions

class Menu(object):

    def __init__(self):
        self.bank = Bank()
        self.exit = False

    def print_header(self):

        print("****************************************************************************")
        print("***********                                            *********************")
        print("***********  Welcome to Jason's Awesome Banking App!!  *********************")
        print("***********                                            *********************")
        print("****************************************************************************")
        print("")

    def print_menu(self):

        print("Please make a selection ")
        print("1. Create a new account")
        print("2. Make a deposit")
        print("3. Make a withdrawal")
        print("4. Show account balance")
        print("0. Exit")
        print("")

    def create_account(self):
        account_type = HelperFunctions.check_valid_account_type("Would you like a checking or savings account? ")
        if not account_type:
            return None
        first_name = HelperFunctions.check_valid_name("What is your first name? ")
        if not first_name:
            return None
        last_name = HelperFunctions.check_valid_name("What is your last name? ")
        if not last_name:
            return None
        ssn = HelperFunctions.check_valid_ssn("What is your social security number? ")
        if not ssn:
            return None
        initial_deposit = HelperFunctions.get_valid_initial_deposit(account_type, "What is your initial deposit? ")
        if not initial_deposit:
            return None

        if account_type == "Checking":
            account = Checking(initial_deposit)
        elif account_type == "Savings":
            account = Savings(initial_deposit)

        customer = Customer(first_name, last_name, ssn, account)
        self.bank.add_customer(customer)

    def make_deposit(self):
        customer = self.bank.select_customer()

        if not customer:
            return None

        account = customer.account
        print("You currently have a balance of {0:.2f}".format(account.balance))
        amount = HelperFunctions.check_positive_float("How much would you like to deposit? ")

        if amount == 0:
            return None

        account.deposit(amount)

        return None

    def make_withdrawal(self):
        customer = self.bank.select_customer()

        if not customer:
            return None

        proceed = HelperFunctions.check_valid_yes_no("Withdrawals incur a $5.00 fee, would you like to proceed? (Y/N) ")

        if not proceed:
            return None

        account = customer.account
        print("You currently have a balance of {0:.2f}".format(account.balance))
        amount = HelperFunctions.check_positive_float("How much would you like to withdraw? ")

        if amount == 0:
            return None

        account.withdraw(amount)

        return None

    def show_balance(self):
        customer = self.bank.select_customer()

        if not customer:
            return None

        print(customer)
        input("Press enter key to continue...")
        print("")
        print("")

        return None

    def exit_menu(self):
        print("Thank you for visiting, see you next time!")
        self.exit = True

    def perform_action(self):

        if self.choice == 1:
            return self.create_account()
        elif self.choice == 2:
            return self.make_deposit()
        elif self.choice == 3:
            return self.make_withdrawal()
        elif self.choice == 4:
            return self.show_balance()
        elif self.choice == 0:
            return self.exit_menu()

    def get_choice(self):
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

    def run_menu(self):
        self.print_header()
        while not self.exit:
            self.print_menu()
            self.choice = self.get_choice()
            self.perform_action()

    def run(self):
        self.run_menu()
