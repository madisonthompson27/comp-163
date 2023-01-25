"""
Madison Thompson
11/16/2022
COMP 163-001
A program that allows a user to enter a list of names, until they choose to terminate it, and adds those names to a files called Roster.txt
"""

#creates the roster file
fileHandle = open("RosterALT.txt", "a")

#allows the user to input their roster
userRoster = input("Enter your roster, with each name seperated by a comma.\nFor example, Madison Thompson, Derrick Leflore.\n")

#splits the roster into a list
splitRoster = userRoster.split(", ")

#iterates through a for loop to add each name to the file
for i in range(0, len(splitRoster)):
    fileHandle.write(str(splitRoster[i]) + "\n")
    i += 1
    
#making sure the file is closed and can be accessed
fileHandle.close()