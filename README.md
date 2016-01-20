# Banking_App
Capital One Coding Challenge

# Jason's Awesome Banking App!
An app that allows you to simulate a bank by allowing a teller to create customers, make deposits, make withdrawals, and check on account customer details.

## Clone the repository

```$ git clone https://github.com/jkeung/Banking_App.git```

## Setup

This code is portable across the following OS's: Linux distributions, Mac and Windows OS's. Scripts were written using Python 2.7 and have not been tested for portability to Python 3.X.

You are encouraged to use a python virtual environment using virtualenv and pip. 

```$ virtualenv venv```

### Install requirements:

```$ pip install -r requirements.txt```

#### Description of modules imported and application

## Run Application

Application can be run by simply running the following shell script from the root directory

```$ source bin/banking_app.sh```

## Instructions

Note: At any time you can cancel the step you are currently in and type '0' to exit.

### 1) Creating a New Account

- On the main menu, create an account by pressing the number ```1```. 
- You will then be prompted to create a Checkings or Savings account. ```"Would you like a checking or savings account?"```
- Type ```"Checking"``` for a Checking Account or type ```"Savings"``` for a Savings account
- You will then be prompted to enter your first name. *A valid first name is one with all alphabetical characters and has no spaces.*
- Enter your ```First Name```
- You will then be prompted to enter your last name. *A valid last name is one with all alphabetical characters and has no spaces.*
- Enter your ```Last Name```
- You will then be prompted to enter your social security number. *A valid last name is a numerical string that contains only numbers or numbers and dashes '123456789' or '123-45-6789'*
- Enter your ```Social Security Number```
- You will then be prompted to enter your initial deposit amount. *A Checking Account requires a minimum of $100.00 to open and A Savings Account requires a minimum of $50.00 to open. (Ex. 100.00 or $100.00)*
- After successfully creating an account, you will return to the menu. 

### 2) Making a Deposit

- On the main menu, make a deposit by pressing the number ```2```. 
- You will then be prompted to select a specific customer from a list of customers in your bank.
- Enter the ```Number of the Customer``` (ex. 1)
- You will then be prompted to enter the amount you would like to deposit. *Checking Accounts do not receive an interest bonus for a deposit.* If you have a Savings account with over $10,000 the interest rate will be set to 5%, otherwise the interest rate will be set to 2%.
- After successfully making a deposit, you will return to the menu.

### 3) Making a Withdrawal

- On the main menu, make a withdrawal by pressing the number ```3```. 
- You will then be prompted to select a specific customer from a list of customers in your bank.
- Enter the ```Number of the Customer``` (ex. 1)
- You will then be prompted to enter the amount you would like to withdraw. *All withdrawals incur a fee of $5.00* If the customer does not have enough money in the account, the withdrawal will not be made due to insufficient funds.
- After successfully making a withdrawal, or if there are insufficient funds, you will return to the menu.

### 4) View Account Details

- On the main menu, view account details by pressing the number ```4```. 
- You will then be prompted to select a specific customer from a list of customers in your bank.
- Enter the ```Number of the Customer``` (ex. 1)
- The customer details will then be shown. Some of the information provided in account details are: First Name, Last Name, SSN, Account Type, Account Number, Balance, and Interest Rate.

### 5) Exit the Application

- On the main menu, view account details by pressing the number ```0```. 

## Next Steps
This application is still a work in progress and a number of items can be added to make this app more robust. A few of the future enhancements are listed below.

- Persist data into a SQL database, currently data is saved and loaded into a Pickle file
- Transfer money between accounts
- Remove accounts
- View recent transactions
- Add more test cases! 