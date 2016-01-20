from __future__ import absolute_import


class DataValidation(object):
    """Data Validation represents a class that contains data validation helper functions

    Attributes:
        None
    Args:
        None

    """
    @staticmethod
    def check_valid_account_type(prompt):
        """Data validation function to check if an account is checking or savings

        Args:
            prompt (string): A prompt that will be given to the user for input

        """
        account_type = raw_input(prompt).title()

        if account_type == '0':
            return None

        if account_type not in ['Checking', 'Savings']:
            print("Please enter 'Checking' or 'Savings'")
            print("")
            account_type = DataValidation.check_valid_account_type(prompt)

        return account_type

    @staticmethod
    def get_valid_initial_deposit(account_type, prompt):
        """Data validation function to check if an account's initial deposit is valid

        Args:
            account_type (string): Indicator if an account is 'Checking' or 'Savings'
            prompt (string): A prompt that will be given to the user for input

        """
        initial_deposit = raw_input(prompt).replace("$","")

        if initial_deposit == 0:
            return None

        if not DataValidation.is_decimal(initial_deposit):
            print("Please enter a numerical value.\n")
            return DataValidation.get_valid_initial_deposit(account_type, prompt)

        initial_deposit = float(initial_deposit)

        if initial_deposit < 0:
            print("Please enter a positive value\n")
            return DataValidation.get_valid_initial_deposit(account_type, prompt)
        elif account_type == 'Checking' and initial_deposit < 100:
            print("Opening a checking account requires a minimum deposit of $100.00\n")
            return DataValidation.get_valid_initial_deposit(account_type, prompt)
        elif account_type == 'Savings' and initial_deposit < 50:
            print("Opening a savings account requires a minimum deposit of $100.00\n")
            return DataValidation.get_valid_initial_deposit(account_type, prompt)

        return initial_deposit

    @staticmethod
    def check_positive_float(prompt):
        """Data validation function to check if an input is a positive float dollar amount

        Args:
            prompt (string): A prompt that will be given to the user for input

        """
        value = raw_input(prompt).replace("$","")

        if value == "0":
            return None

        if not DataValidation.is_decimal(value):
            print("Please enter a numerical value. \n")
            return DataValidation.check_positive_float(prompt)

        value = float(value)

        if value < 0:
            print("Please enter a positive value. \n")
            return DataValidation.check_positive_float(prompt)

        return value

    @staticmethod
    def check_valid_name(prompt):
        """Data validation function to check if an input is a valid name with no numbers or spaces

        Args:
            prompt (string): A prompt that will be given to the user for input

        """
        text = raw_input(prompt)
        if text == "0":
            return None
        if not text.isalpha():
            print("Enter valid name, no numbers or spaces are allowed \n")
            return DataValidation.check_valid_name(prompt)


        return text

    @staticmethod
    def check_valid_ssn(prompt):
        """Data validation function to check if an input is a valid social security number

        Args:
            prompt (string): A prompt that will be given to the user for input

        """
        ssn = raw_input(prompt).replace("-","")
        if ssn == '0':
            return None

        if not (len(ssn) == 9 and ssn.isdigit()):
            print("Please enter a valid social security number (ex. 123-45-6789)\n")
            return DataValidation.check_valid_ssn(prompt)

        return ssn

    @staticmethod
    def check_valid_yes_no(prompt):
        """Data validation function to check if an input is a valid option (Y/N)

        Args:
            prompt (string): A prompt that will be given to the user for input

        """
        choice = raw_input(prompt).lower()
        if choice == '0':
            return None

        if choice in ["n", "no"]:
            print("Transaction cancelled. \n")
            return None
        elif choice not in ["y", "yes", "n", "no"]:
            print("Please enter a valid selection (Y/N) \n")
            return DataValidation.check_valid_yes_no(prompt)

        return choice

    @staticmethod
    def is_decimal(text):
        """Data validation function to check if a string is a float

        Args:
            text (string): A text input

        """
        try:
            float(text)
            return True
        except ValueError:
            return False
