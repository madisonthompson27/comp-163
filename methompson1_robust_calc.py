"""
Madison Thompson
11/11/2022
COMP 163-001
A program that does not break due to the incorporation of custom exceptions and try/except blocks. Calls on a while loop and boolean
determiniations to execute according to error status in a user-friendly way, until the user enters the sentinel value. 
"""

#creating a custom exception to catch errors unique from standard python lib
class AggieCalcError(Exception):
    def __init__(self):
        super().__init__("Invalid range. Numbers must be between 500 and 1000 (inclusive).")

#defining functions that will be used if selected by user in menu
#functions not in class

    #f-strings allow users to understand results and prevent confusion in case of misclicks in menu
def add(value1, value2):
    mySum = value1 + value2
    print(f'Your sum is: {mySum}')

def subtract(value1, value2):
    myDifference = value1 - value2
    print(f'Your difference is: {myDifference}')

def multiply(value1, value2):
    myProduct = value1 * value2
    print(f'Your product is {myProduct}')

#does not use floor division, values can be ints or floats
def divide(value1, value2):
    myQuotient = value1 / value2
    print(f'Your quotient is: {myQuotient}')

#initializing boolean to be used to determine if functions will execute in loop
restart = False

#making display menu with multiple choice options. user will be prompted to pick an option following menu display. 
while True:
    
    #resets boolean  value for each iteration
    restart = False
    
    #displays menu 
    print()
    print('Type 1 to add')
    print('Type 2 to subtract')
    print('Type 3 to multiply')
    print('Type 4 to divide')
    print('Type 5 to quit\n')

    #userSelection variable determines what operation is performed    
    try:
        userSelection = str(input('Type your menu selection: '))
        
        #if loop quits before values are entered to avoid user frustration 
        if userSelection == "5":
            break

        if userSelection != "1" and userSelection != "2" and userSelection != "3" and userSelection != "4" and userSelection != "5":
            raise ValueError()
    
    except ValueError:
        print()
        print("Menu selection must be a single character between 1 and 5.")
        restart = True
 
    #final catch all
    except Exception:
        print("Bad data")
        restart = True
    
    #running if statement to test if restart == True. If so, loop passes next block due to errors. 
    if restart == True:
        pass
    
    #if no errors occurred in the first block, continue with execution.
    else:
        try:
            print()
            #users can enter new values as they wish, in order to allow them to adapt to the menu's repeating options
            userValue1 = int(input('Enter your first value: '))
            userValue2 = int(input('Enter your second value: '))
    
            #validating range
            if userValue1 not in range(500, 1001):
                raise AggieCalcError()
        
            if userValue2 not in range(500, 1001):
                raise AggieCalcError()
        
        except AggieCalcError as excpt:
        
            #provides spacing to make error message clearly visbile 
            print()
        
            #prints exception message
            print(excpt)
            restart = True
    
        #ensuring no floats or strings are passed
        except ValueError or TypeError:
            print()
            print("Values must be an integer with no decimal place") 
            restart = True


        #final catch all
        except Exception:
            print("Bad data")
            restart = True

    #verifying that errors were not raised before executing functions
    if restart == True:
        pass
    
    #series of if statements allow for the proper function to be enacted dependent on user selection
    else:
        if userSelection == "1":
            add(userValue1, userValue2)
            
        if userSelection == "2":
            subtract(userValue1, userValue2)
        
        if userSelection == "3":
            multiply(userValue1, userValue2)
        
        if userSelection == "4": 
            divide(userValue1, userValue2)

#loop does not terminate, will repeat unti userSelection == "5"