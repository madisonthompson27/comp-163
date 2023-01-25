#  Madison Thompson
#  COMP-163 : Section 001
#  Instructor : Derrick Leflore
#  Description : GUI program that can be imported as a method into other files. Used to prompt the user through possible behaviors. 

#importing bankAccount to be referenced for program initialization
import methompson1_BankAccount as BA

#showMenu function initialization
def showMenu():
    
    #proper spacing as stated in instructions
    print()
    print()
    
    #menu options
    print("A. Check Balance")
    print("B. Deposit")
    print("C. Withdraw")
    print("D. Previous Balance")
    print("E. Exit")

#testing
#showMenu() #testing was effective as of 10/31/2022

#function to read user input after showMenu() and output as a usable value for subsequent functions
def getMenuOption():
        
    #allows user to make a choice, seperate from display options because it needs to be repeated
    print("====================================================================================================")
    print("Enter an option") #input not read here because all lines will not print accurately
    print("====================================================================================================")
    
    #no prompt is given because it is alreay provided in line 28, .upper() reduces risk for human error
    userSelection = str(input()).upper()
    
    #formatting code to match template provided
    print()
    print()
    return userSelection

#testing
#getMenuOption() #testing was effective as of 10/31/2022


##START PROGRAM INITIALIZATION##

if __name__ == "__main__":
    
    #assigning customerAccount with BankAccount() class
    customerAccount = BA.BankAccount()
    #customerAccount = BankAccount(customerName, customerId)

    #uses earlier called functions to show menu value and allow the user to select a menu option
    showMenu()
    userMenuOption = getMenuOption()

    #while loop allows the user to interact with their account until they choose to quit
    while userMenuOption != 'E': 
        
        #menu option A allows the user to check their balance
        if userMenuOption =='A':
            
            #all balances start at 0. There must be a deposit first. so, customerAccount.setBalance() should return 0 if first called. 
            customerAccount.getBalance()
        
        #menu option B allows the user to make a deposit
        if userMenuOption == 'B':
            customerAccount.deposit()
        
        #menu option C allows the user to make a withdrawl
        if userMenuOption == 'C':
            customerAccount.withdraw()

        #menu option D allows the user to view their previous transaction and previous balance
        if userMenuOption == 'D':
            customerAccount.getPreviousTransaction()
        
        #menu option E allows the user to exit the account. while loop should catch it, failsafe just in case. 
        if userMenuOption == 'E':
            break
        
        #allows the user to select another menu option within while loop (will break if userMenuOption == "E")
        userMenuOption = getMenuOption()    
            
#exit message
print(f'Thank you {customerAccount.customerName} for using Aggie Bank')

#notes: is second constructor needed or is it just for 167 students?? how to implement?