"""
Madison Thompson
11/16/2022
COMP 163-001
A program that allows a user to enter a list of names, until they choose to terminate it, and adds those names to a files called Roster.txt
"""

#creates the roster file
fileHandle = open("Roster.txt", "a")

#allows the user to decide if they would like to continue, through while loop and boolean determination
nextName = True

#start while loop
while nextName == True:
    
    #trying to read it as a string
    rosterName = str(input("Enter first and last name or type Q to quit: "))
    
    #if the user inputs Q to quit, the loop will break. otherwise it writes to the file. 
    if rosterName == "Q":
        nextName = False
        break
    
    #works for upper and lower Q
    elif rosterName == "q":
        nextName = False
        break
    
    #adds roster name to file, concatenation possible because of str type
    else:
        fileHandle.write(rosterName + "\n")
        #failsafe boolean verification
        nextName = True
        
#making sure the file closes and can be accessed
fileHandle.close()