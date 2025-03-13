class Bank:
    # Class attributes (Static Variables)
    name = 'SBI'   # Bank name
    addr = 'Noida' # Bank location
    branch = 'Sec 16' # Bank branch
    
    def __init__(self, name, adhar, phn):
        """
        Constructor to initialize instance attributes.
        These attributes are unique to each object.
        """
        self.name = name  # Customer name
        self.adhar = adhar  # Aadhar number
        self.phn = phn  # Phone number

    def show_details(self):
        """
        Instance method to display customer details.
        """
        print(f"Name: {self.name}, Phone Number: {self.phn}")

    def change_no(self):
        """
        Instance method to update the phone number.
        """
        self.phn = int(input("Enter a new number: "))

    @classmethod
    def bank_info(cls):
        """
        Class method to display bank details.
        """
        print(f"Bank Name: {cls.name}, Branch: {cls.branch}")

    @classmethod
    def change_branch(cls, new):
        """
        Class method to change the branch of the bank.
        """
        cls.branch = new
    
    @staticmethod
    def method():
        """
        Static method (not related to instance or class attributes).
        It can be used for utility purposes.
        """
        print("This is a static method, independent of class and instance variables.")

# Creating an instance of Bank class
ob1 = Bank('Abhishek', 2422, 12345678)

# Displaying customer details
ob1.show_details()

# Uncomment to modify phone number
# print('Modify details')
# ob1.change_no()
# ob1.show_details()

# Displaying bank information
Bank.bank_info()

# Changing branch using class method
Bank.change_branch("Sec 52")
Bank.bank_info()

# Calling static method
Bank.method()
