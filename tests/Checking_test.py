import unittest

from banking.Checking import Checking


class TestChecking(unittest.TestCase):

    def test_create_checking_accounts(self):
        test_account1 = Checking(100)

        self.assertGreaterEqual(test_account1.account_number, 1000000)
        self.assertEquals(test_account1.balance, 100)
        self.assertEquals(test_account1.account_type, "Checking")
        self.assertEquals(test_account1.interest_rate, 0)

    def test_withdraw(self):
        test_account1 = Checking(100)
        test_account1.withdraw(50)

        self.assertEqual(test_account1.balance, 45)

    def test_deposit(self):
        test_account1 = Checking(100)
        test_account1.deposit(100)

        self.assertEqual(test_account1.balance, 200)

    def test_withdraw_string(self):
        test_account1 = Checking(100)

        with self.assertRaises(TypeError):
            test_account1.withdraw('blah')

    def test_deposit_string(self):
        test_account1 = Checking(100)

        with self.assertRaises(TypeError):
            test_account1.deposit('blahblah')

    def test_withdraw_none(self):
        test_account1 = Checking(100)

        with self.assertRaises(TypeError):
            test_account1.withdraw()

    def test_deposit_none(self):
        test_account1 = Checking(100)

        with self.assertRaises(TypeError):
            test_account1.deposit()

    def test_withdraw_negative(self):
        test_account1 = Checking(100)

        self.assertEquals(test_account1.withdraw(-100), None)

    def test_deposit_negative(self):
        test_account1 = Checking(100)

        self.assertEquals(test_account1.deposit(-1), None)

if __name__ == '__main__':
    unittest.main()

