#  Madison Thompson
#  COMP-163 : Section 001
#  Instructor : Derrick Leflore
#  Description : uses imported module to allow a user to use modifiers that will manipulate their bank account information


##START CLASS DECLARATION##

#class declaration instantchiates reference variables by type
class BankAccount:
    balance = 0
    customerId = 0
    customerName = ""
    previousTransaction = 0
 
 #constructor for class BankAccount that prints first screen and assigns inputed values to the function
    def __init__(self, *inp):
        
        #if statements check to see which version of constructor needs to run since python doesn't allow two constructors
            #based on if the user provides their name and id or not. will prompt if not provided. 
        
        #prints starting message to read input values when inp == 0
        if len(inp) == 0:
            print("****************************************************************************************************")
            print("Aggie Bank Account")
            
            #uses functions to find customerName and customerId so that they're easier to access later on
            customerName = self.getCustomerName()
            customerId = self.getCustomerId()
            
            #initializing values that were read as inputs. inside of if statement to prevent reference before assignment error. 
            self.customerName = customerName
            self.customerId = customerId
        
        #checks for input length 2, which would be customer name and customer ID given
        elif len(inp) == 2:
            self.knownCustomerInfo(inp)
        
        #standard spacing
        print()
        print()
        
        #printing welcome message after values are acquired, regardless of input len
        print("****************************************************************************************************")
        print(f'Welcome {self.customerName}')
        print(f'Your ID is {self.customerId}')
    
    #defining function to execute when customer info is already known
    def knownCustomerInfo(self, args):
        
        #assigning argument values to already instantchiated reference variables. self.var eliminates need for future assignment
        self.customerName = args[0]
        self.customerId = args[1]
        
        #printing standard statement with values provided so they can be used later in constructor
        print("****************************************************************************************************")
        print("Aggie Bank Account")
        print(f'Enter customer name : ', self.customerName)
        print(f'Enter customer ID : ', self.customerId)

#testing to make sure both versions of constructor run properly
#TESTuserInformation1 = BankAccount() #effective through class as of 11/01/2022
#TESTuserInformation2 = BankAccount("Moo", 12345) #effective through class as of 11/01/2022

#series of modifiers that allow the user to interact with their bank account (deposit, withdraw, etc.)

    #prompts customer for name
    def getCustomerName(self):
        customerName = str(input("Enter customer name: ")).title()
        return customerName
    
    #sets customer name to value recieved in getCustomerName()
    def setCustomerName(self, customerName):
        self.customerName = customerName
        return self.customerName
    
    #calcuates customer account value based on withdrawls and deposits
    def getBalance(self):
        
        #outputs the users account balance
        print(f'Current Account Balance: {self.balance}')
    
    #sets current account balance. variations of setBalance() are used for deposit() and withdraw()
    def setBalance(self, balance):
        self.balance = balance
    
    #prompts customer for ID
    def getCustomerId(self):
        self.customerId = input("Enter customer ID: ")
        return self.customerId

    #sets customer ID to value recieved in getCustomerId()
    def setCustomerId(self, customerId):
        self.customerId = customerId
    
    #allows the user to review their last action (once one has occured)
    def getPreviousTransaction(self):
        
        #checking to see if a transaction has occured already
        print("----------------------------------------------------------------------------------------------------")
        if self.balance == 0:
            #means that balance is same as instantchiation value
            print("No transaction occured")
            
        #prevBalance is used in deposit and withdraw as a tempvar to hold previous balance for inequality
        elif self.prevBalance > self.balance:
            #allows the user to view their account balance prior to the previous transaction and withdrawl value (not reflected)
            print(f'Withdrawn: {self.withdrawVal}')
        
        elif self.prevBalance < self.balance:
            #allows the user to view their account balance prior to the previous transaction and the deposit value (not reflected)
            print(f'Deposited: {self.depositVal}')
        print("----------------------------------------------------------------------------------------------------")
        
    #sets and returns the value of the previous transaction
    def setPreviousTransaction(self):
        self.balance += self.previousTransaction
        return self.balance
    
    #takes the desired amount of money out of the account (subtracts from balance)
    def withdraw(self):
        print("----------------------------------------------------------------------------------------------------")
        print("Enter amount to withdraw")
        print("----------------------------------------------------------------------------------------------------")
        
        #user input value comes after statement is printed within dashes
        withdrawVal = int(input())
        
        #making withdrawVal part of the self class so it can be called on by previous transaction functions
        self.withdrawVal = withdrawVal
        self.prevBalance = self.balance
        
        #updating balance value to reflect changes caused by withdrawVal
        self.balance -= withdrawVal
    
    #adds the desired amount of money to the account (adds to balance)
    def deposit(self):
        print("----------------------------------------------------------------------------------------------------")
        print("Enter amount to deposit")
        print("----------------------------------------------------------------------------------------------------")
        depositVal = int(input())
         
        #making depositVal part of the self class so it can be called by previous transaction functions
        self.depositVal = depositVal
        self.prevBalance = self.balance
        
        #updating balance value to reflect changes caused by depositVal
        self.balance += depositVal