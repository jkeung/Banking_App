import unittest
from Savings import Savings


class TestSavings(unittest.TestCase):

    def test_create_checking_accounts_low_interest(self):
        test_account1 = Savings(100)

        self.assertGreaterEqual(test_account1.account_number, 1000000)
        self.assertEquals(test_account1.balance, 100)
        self.assertEquals(test_account1.account_type, "Savings")
        self.assertEquals(test_account1.interest_rate, .02)

    def test_create_checking_accounts_borderline_interest(self):
        test_account1 = Savings(10000)

        self.assertGreaterEqual(test_account1.account_number, 1000000)
        self.assertEquals(test_account1.balance, 10000)
        self.assertEquals(test_account1.account_type, "Savings")
        self.assertEquals(test_account1.interest_rate, .02)

    def test_create_checking_accounts_high_interest(self):
        test_account1 = Savings(10001)

        self.assertGreaterEqual(test_account1.account_number, 1000000)
        self.assertEquals(test_account1.balance, 10001)
        self.assertEquals(test_account1.account_type, "Savings")
        self.assertEquals(test_account1.interest_rate, .05)

    def test_withdraw(self):
        test_account1 = Savings(100)
        test_account1.withdraw(50)

        self.assertEqual(test_account1.balance, 45)

    def test_deposit(self):
        test_account1 = Savings(100)
        test_account1.deposit(100)

        self.assertEqual(test_account1.balance, 200 + 100*.02)

    def test_withdraw_string(self):
        test_account1 = Savings(100)

        with self.assertRaises(TypeError):
            test_account1.withdraw('blah')

    def test_deposit_string(self):
        test_account1 = Savings(100)

        with self.assertRaises(TypeError):
            test_account1.deposit('blahblah')

    def test_withdraw_none(self):
        test_account1 = Savings(100)

        with self.assertRaises(TypeError):
            test_account1.withdraw()

    def test_deposit_none(self):
        test_account1 = Savings(100)

        with self.assertRaises(TypeError):
            test_account1.deposit()

    def test_withdraw_negative(self):
        test_account1 = Savings(100)

        self.assertEquals(test_account1.withdraw(-100), None)

    def test_deposit_negative(self):
        test_account1 = Savings(100)

        self.assertEquals(test_account1.deposit(-1), None)

if __name__ == '__main__':
    unittest.main()

