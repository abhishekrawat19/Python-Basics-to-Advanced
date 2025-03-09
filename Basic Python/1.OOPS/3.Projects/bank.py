from abc import ABC, abstractmethod

# Abstract Class for ATM Operations
class ATM(ABC):
    
    def __init__(self, balance=0):
        self._balance = balance  # Private variable for balance
    
    @abstractmethod
    def deposit(self, amount):
        pass  
    
    @abstractmethod
    def withdraw(self, amount):
        pass
    
    @abstractmethod
    def check_balance(self):
        pass

# Concrete ATM Class
class BankATM(ATM):
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount. Please enter a positive number.")
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive number.")
        elif amount > self._balance:
            print("Insufficient balance.")
        else:
            self._balance -= amount
            print(f"₹{amount} withdrawn successfully.")
    
    def check_balance(self):
        print(f"Your current balance is ₹{self._balance}")

# ATM Simulation
atm = BankATM(5000)  # Initial balance ₹5000

while True:
    print("\nATM Menu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        try:
            amount = float(input("Enter deposit amount: "))
            atm.deposit(amount)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    elif choice == '2':
        try:
            amount = float(input("Enter withdrawal amount: "))
            atm.withdraw(amount)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    elif choice == '3':
        atm.check_balance()
    
    elif choice == '4':
        print("Thank you for using the ATM. Have a great day!")
        break
    
    else:
        print("Invalid choice. Please try again.")
