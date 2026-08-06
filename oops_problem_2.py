'''
The Problem: Bank Account Management System

You are building the backend logic for a simple banking application. The system
should manage different types of bank accounts while ensuring that account
details and balances are handled securely.

=============================================================================
Phase 1: The Parent Class (Account)

Create a base class named Account.

Attributes:
account_holder (string) — e.g., "Aman"
account_number (string) — e.g., "ACC101"
__balance (private) — Defaults to 0 unless specified.

Methods:
deposit(amount)
    - Adds money to the account.
    - Reject deposits of 0 or negative amounts.

withdraw(amount)
    - Removes money from the account.
    - Reject withdrawal if amount is greater than the available balance.

get_balance()
    - Returns the current balance safely.

=============================================================================
Phase 2: Class Attribute & Class Method

Keep track of how many accounts have been created.

Requirements:
Create a class variable named account_count.

Whenever a new Account (or child account) is created,
increase this counter.

Create a class method:
total_accounts()
    - Returns the total number of accounts created.

=============================================================================
Phase 3: Inheritance

Create two child classes that inherit from Account.

SavingsAccount

Additional Attribute:
interest_rate (percentage)

Additional Method:
add_interest()
    - Calculates interest using the current balance.
    - Adds the interest amount to the balance.

------------------------------------------------------------

CurrentAccount

Additional Attribute:
overdraft_limit

Override the withdraw() method.

Unlike a normal account, a current account can have
a negative balance up to the overdraft limit.

Example:

Balance = ₹2000
Overdraft Limit = ₹3000

Maximum withdrawal allowed = ₹5000

If the withdrawal exceeds the overdraft limit,
print "Overdraft limit exceeded."

=============================================================================
Phase 4: Polymorphism

Create a list containing different account objects.

Call withdraw() on every object using a loop.

Notice how the same method behaves differently for
different account types.

=============================================================================
Phase 5: Magic Method

Implement the __str__() method.

Printing an account object should display something like:

Aman's Account (ACC101) - Balance: ₹5000

=============================================================================
Phase 6: Putting it to the Test (Expected Output)

Write a program that:

1. Creates a normal Account.
2. Deposits and withdraws money.
3. Creates a SavingsAccount and adds interest.
4. Creates a CurrentAccount and tests overdraft.
5. Prints all account details.
6. Prints the total number of accounts.
7. Demonstrates polymorphism by calling withdraw()
    on all account objects inside a loop.

Need a hint on how to start?

Remember to use super().__init__() inside the child
classes so they inherit the account holder,
account number, and balance from the Account class.
'''

# ====================================================================
# Solution
# ====================================================================

# ====================================================================
# Phase 1: Parent Class (Account)
# ====================================================================

class Account:

    # Class variable to keep track of total accounts created
    account_count = 0

    # Constructor
    def __init__(self, account_holder, account_number, balance=0):

        # Store account holder name
        self.account_holder = account_holder

        # Store account number
        self.account_number = account_number

        # Private balance (cannot be accessed directly outside the class)
        self.__balance = balance

        # Increase account count whenever a new account is created
        Account.account_count += 1


    # Method to deposit money
    def deposit(self, amount):

        # Deposit amount should be greater than 0
        if amount <= 0:
            print("Invalid deposit amount.")

        else:
            # Add amount to balance
            self.__balance += amount
            print("₹{} deposited successfully.".format(amount))


    # Method to withdraw money
    def withdraw(self, amount):

        # Withdrawal amount should be greater than 0
        if amount <= 0:
            print("Invalid withdrawal amount.")

        # Check if enough balance is available
        elif amount > self.__balance:
            print("Insufficient balance.")

        else:
            # Subtract money from balance
            self.__balance -= amount
            print("₹{} withdrawn successfully.".format(amount))


    # Getter method to safely access balance
    def get_balance(self):
        return self.__balance


    # Protected helper method
    # Used by child classes to update balance
    def _set_balance(self, amount):
        self.__balance = amount


    # Class method to return total accounts created
    @classmethod
    def total_accounts(cls):
        return cls.account_count


    # Magic method to display account details in a readable format
    def __str__(self):

        return "{}'s Account ({}) - Balance: ₹{}".format(
            self.account_holder,
            self.account_number,
            self.get_balance()
        )


# ====================================================================
# Phase 2: Inheritance
# ====================================================================

# Child Class - Savings Account
class SavingsAccount(Account):

    # Constructor
    def __init__(self, account_holder, account_number, interest_rate, balance=0):

        # Call parent class constructor
        super().__init__(account_holder, account_number, balance)

        # Additional attribute for Savings Account
        self.interest_rate = interest_rate


    # Method to add interest to the account
    def add_interest(self):

        # Calculate interest
        interest = self.get_balance() * self.interest_rate / 100

        # Calculate new balance
        new_balance = self.get_balance() + interest

        # Update balance using protected method
        self._set_balance(new_balance)

        print("Interest of ₹{:.2f} added.".format(interest))


# --------------------------------------------------------------------


# Child Class - Current Account
class CurrentAccount(Account):

    # Constructor
    def __init__(self, account_holder, account_number, overdraft_limit, balance=0):

        # Call parent class constructor
        super().__init__(account_holder, account_number, balance)

        # Additional attribute for Current Account
        self.overdraft_limit = overdraft_limit


    # Overriding withdraw() method
    # Current Account allows overdraft
    def withdraw(self, amount):

        # Withdrawal amount should be greater than 0
        if amount <= 0:
            print("Invalid withdrawal amount.")

        else:

            # Calculate balance after withdrawal
            remaining_balance = self.get_balance() - amount

            # Check if overdraft limit is crossed
            if remaining_balance < -self.overdraft_limit:
                print("Overdraft limit exceeded.")

            else:
                # Update balance
                self._set_balance(remaining_balance)

                print("₹{} withdrawn successfully.".format(amount))


# ====================================================================
# Phase 3: Testing
# ====================================================================

print("---------- Normal Account ----------")

# Create a normal account
acc1 = Account("Aman", "ACC101", 5000)

# Deposit money
acc1.deposit(1000)

# Withdraw money
acc1.withdraw(2000)

# Print current balance
print("Current Balance:", acc1.get_balance())


print("\n---------- Savings Account ----------")

# Create a savings account
acc2 = SavingsAccount("Rahul", "SAV201", 5, 10000)

# Add interest
acc2.add_interest()

# Print current balance
print("Current Balance:", acc2.get_balance())


print("\n---------- Current Account ----------")

# Create a current account
acc3 = CurrentAccount("Riya", "CUR301", 3000, 2000)

# Withdraw using overdraft facility
acc3.withdraw(4000)

# Try to withdraw more than overdraft limit
acc3.withdraw(2000)

# Print current balance
print("Current Balance:", acc3.get_balance())


print("\n---------- Account Details ----------")

# __str__() is called automatically when using print()
print(acc1)
print(acc2)
print(acc3)


print("\n---------- Total Accounts ----------")

# Print total accounts created
print(Account.total_accounts())


print("\n---------- Polymorphism ----------")

# Store different account objects inside one list
accounts = [acc1, acc2, acc3]

# Same method call behaves differently for different objects
for account in accounts:

    print("\n", account)

    # Calls the appropriate withdraw() method
    account.withdraw(3000)

    # Print updated balance
    print("Balance:", account.get_balance())