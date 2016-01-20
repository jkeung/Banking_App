import unittest
from Bank import Bank
from Customer import Customer
from Account import Account


class TestSavings(unittest.TestCase):

    def test_create_bank(self):
        bank = Bank()
        self.assertEquals(bank.customers, [])

    def test_create_bank_with_negative_params(self):
        with self.assertRaises(TypeError):
            bank = Bank(-1)

    def test_add_customer(self):

        bank = Bank()
        account = Account(100)
        customer = Customer('john', 'smith', '123456789', account)
        bank.add_customer(customer)
        self.assertEquals(bank.customers[0], customer)
        self.assertEquals(bank.customers[0].first_name, 'john')
        self.assertEquals(bank.customers[0].last_name, 'smith')
        self.assertEquals(bank.customers[0].ssn, '123456789')
        self.assertEquals(bank.customers[0].account.balance, 100)

    def test_select_customer(self):

        bank = Bank()
        account = Account(100)
        customer = Customer('john', 'smith', '123456789', account)
        bank.add_customer(customer)
        bank.select_customer()





if __name__ == '__main__':
    unittest.main()