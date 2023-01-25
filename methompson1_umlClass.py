#  Madison Thompson
#  COMP-163 : Section 001
#  Instructor : Derrick Leflore
#  Description : using one class to prompt the user to enter bank account information and display changes in monetary values

class BankAccount:
    balance = 0
    customerId = 0
    customerName = ""
    previousTransaction = 0
    
    # Constructor
    def __init__(self, customerName=" ", customerId=0, previousTransaction=0):
        self.customerId = customerId
        self.customerName = customerName
        self.previousTransaction = previousTransaction
        self.balance
    
    def getCustomerName(self):
        self.customerName = str(input("Enter customer name: "))
    
    def setCustomerName(self, customerName):
        self.customerName = customerName
        return self.customerName
    
    def getBalance(self):
        self.balance = int(input("Current account balance: "))
        return self.balance
    
    def setBalance(self, balance):
        self.balance = balance
    
    def getCustomerId(self):
        self.customerId = int(input("Enter customer ID: "))
        return self.customerId

    def setCustomerId(self, customerId):
        self.customerId = customerId
    
    def getPreviousTransaction(self):
        self.previousTransaction = int(input("Enter value of previous transaction: "))
    
    def setPreviousTransaction(self):
        self.balance += self.previousTransaction
        return self.balance
    
    def withdraw(self):
        withdraw = int(input("Enter amount to withdraw: "))
        self.balance -= withdraw
    
    def deposit(self):
        deposit = int(input("Enter amount to deposit: "))
        self.balance += deposit

    def printInfo(self):
        print(f'Customer name: {self.customerName}\nCustomer ID: {self.customerId}\nBalance: {self.balance}\n')
    
    
if __name__ == "__main__":
    customerAccount = BankAccount()
    customerName = customerAccount.getCustomerName()
    customerId = customerAccount.getCustomerId()
    balance = customerAccount.getBalance()
    previousTransaction = customerAccount.setPreviousTransaction()    
    deposit = customerAccount.deposit()
    withdraw = customerAccount.withdraw()
    customerAccount.printInfo()