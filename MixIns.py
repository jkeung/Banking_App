__author__ = 'jkeung'


class HelperFunctions(object):

    @staticmethod
    def check_valid_account_type(prompt):
        account_type = ""

        while account_type not in ['Checking', 'Savings']:
            account_type = input(prompt).title()

            if account_type == '0':
                return None

            if account_type not in ['Checking', 'Savings']:
                print("Please enter 'Checking' or 'Savings'")
                print("")

        return account_type

    @staticmethod
    def get_valid_initial_deposit(account_type, prompt):
        # get valid initial deposit
        initial_deposit = -1
        while initial_deposit < 0:
            try:
                initial_deposit = float(raw_input(prompt).replace("$",""))
                print("")

                if initial_deposit == 0:
                    return None
                elif initial_deposit < 0:
                    print("Please enter a positive value")
                    print("")
                elif account_type == 'Checking' and initial_deposit < 100:
                    print("Opening a checking account requires a minimum deposit of $100.00")
                    print("")
                    initial_deposit = -1
                elif account_type == 'Savings' and initial_deposit < 50:
                    print("Opening a savings account requires a minimum deposit of $100.00")
                    print("")
                    initial_deposit = -1

            except ValueError:
                print("Please enter a numerical value.")
                print("")

        return initial_deposit

    @staticmethod
    def check_positive_float(prompt):

        value = -1
        while value < 0:
            try:
                value = float(raw_input(prompt).replace("$",""))

                if value == 0:
                    return None
                elif value < 0:
                    print("Please enter a positive value. ")
                    print("")

            except ValueError:
                print("Please enter a numerical value. ")
                print("")

        return value

    @staticmethod
    def check_valid_name(prompt):

        text = ""

        while not text.isalpha():
            text = raw_input(prompt)
            if text == "0":
                return None

            if not text.isalpha():
                print("Enter valid name, no numbers or spaces are allowed")
                print("")

        return text

    @staticmethod
    def check_valid_ssn(prompt):

        ssn = ""

        while not (len(ssn) == 9 and ssn.isdigit()):
            ssn = raw_input(prompt).replace("-","")
            if ssn == '0':
                return None

            if not (len(ssn) == 9 and ssn.isdigit()):
                print("Please enter a valid social security number (ex. 123-45-6789)")
                print("")

        return ssn

    @staticmethod
    def check_valid_yes_no(prompt):

        choice = ""

        while choice not in ["y", "yes", "n", "no"]:
            choice = raw_input(prompt).lower()
            if choice == '0':
                return None
            elif choice in ["n", "no"]:
                print("Transaction cancelled. ")
                print("")
                return None
            elif choice not in ["y", "yes", "n", "no"]:
                print("Please enter a valid selection (Y/N) ")
                print("")

        return choice
