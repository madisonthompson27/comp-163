"""
Madison Thompson
11/18/2022
COMP 163-001
A modular roster program that allows users to overwrite old rosters, append existing rosters, and display the values of the text file
through the use of infinite loops and if statements. 
"""

#creating menu to be used in while loop
def ShowMenu():
    print()
    print("A) Create new roster")
    print("B) Add to current roster")
    print("C) Print roster")
    print("Q) Exit")
    print()

#function for menu option A to create a new roster (including the original)
def CreateRoster():
    
    #opens new file
    roster = open("roster.txt", "w")
    
    #spacing and prompt
    print()
    print("Enter roster name, or \"X\" to quit: ")
    
    #start while loop to populate roster
    while True: 
        name = input("Enter name: ")
        
        if name.upper() == "X":
            #file will close only when the user has finished inputting values
            roster.close()
            break
        
        roster.write(name + "\n")


#defining a function to allow the user to add names to a roster, could work as the original roster as well 
def AppendRoster():
    
    #creates a new file that overwrites the old one
    roster = open("roster.txt", "a")
    
    #spacing and prompt
    print()
    print("Enter roster name, or \"X\" to quit: ")
    
    #start while loop to populate roster
    while True: 
        name = input("Enter name: ")
        
        if name.upper() == "X":
            #closing roster only when the loop is broken
            roster.close()
            break
        
        roster.write(name + "\n")


#defining a function to display the roster to the user
def PrintRoster():
    
    #reads all values from the roster
    roster = open("roster.txt", "r")
    
    #iterates through roster to print
    for rosterName in roster:
        print(rosterName)

while True:
    #menu will display at the beginning of each iteration
    ShowMenu()
    
    option = input("Enter menu option: ").upper()
    
    #using user input to determine if loop should continue to execute
    if option == "Q":
        break
    
    #calling on menu options
    #option A allows the user to create a new roster by overwriting the old one 
    elif option == "A":
        CreateRoster()
    
    #allowing user to append the roster
    elif option == "B":
        AppendRoster()
    
    #allowing user to print roster
    elif option == "C":
        PrintRoster()
    
    #failsafe final statement
    else:
        print("Invalid option")
    
#exit message after break
print("Goodbye")    