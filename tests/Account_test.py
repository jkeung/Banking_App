#!/usr/bin/env python
from __future__ import absolute_import
import unittest
from banking.Account import Account


class TestAccount(unittest.TestCase):

    def test_two_base_class_accounts(self):
        test_account1 = Account(100)
        self.assertGreaterEqual(test_account1.account_number, 1000000)

    def test_withdraw(self):
        test_account1 = Account(100)
        test_account1.withdraw(50)

        self.assertEquals(test_account1.balance, 45)

    def test_deposit(self):
        test_account1 = Account(100)
        test_account1.deposit(100)

        self.assertEquals(test_account1.balance, 200)

    def test_withdraw_no_amount(self):
        test_account1 = Account(100)

        with self.assertRaises(TypeError):
            test_account1.withdraw()

    def test_deposit_no_amount(self):
        test_account1 = Account(100)

        with self.assertRaises(TypeError):
            test_account1.deposit()

    def test_withdraw_string(self):
        test_account1 = Account(100)

        with self.assertRaises(TypeError):
            test_account1.withdraw('hello')

    def test_deposit_string(self):
        test_account1 = Account(100)

        with self.assertRaises(TypeError):
            test_account1.deposit('hello')

    def test_withdraw_negative(self):
        test_account1 = Account(100)

        self.assertEquals(test_account1.withdraw(-100), None)

    def test_deposit_negative(self):
        test_account1 = Account(100)

        self.assertEquals(test_account1.deposit(-50), None)

if __name__ == '__main__':
    unittest.main()

