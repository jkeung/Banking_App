__author__ = 'jkeung'


class Bank(object):

    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def select_customer(self):

        selection = -1

        if not self.customers:
            print("You have no customers, please create some. \n")
            return None

        while selection not in range(len(self.customers)):

            for i, customer in enumerate(self.customers):
                print("{0}. {1}".format(i+1, customer.display_info()))
            print()

            try:
                selection = int(raw_input("Please select an account: "))
                if selection == 0:
                    return None

                assert selection > 0
                return self.customers[selection-1]
            except (IndexError, AssertionError):
                print("Please specify a number from the list of customers. \n")

        return None
