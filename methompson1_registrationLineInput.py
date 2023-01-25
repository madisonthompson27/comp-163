'''
Madison Thompson
9/29/2022
COMP 163-001
This program uses type conversions, for loops, and string joining to ensure that a for loop iterates through the user-entered list size
and user-entered values for the line position values of consecutive aggies. The program will find the smallest difference between values,
output the smallest difference between values for that entry, and prompt the user to quit or begin again.  
'''

#initializing reference variables
positionInLine = []
finalAggie = []
x = 0

#size of line, will be used to determine how many iterations are ran following input validation
numAggie = int(input("Enter number of Aggies in line: "))

#assigns characters to finalAggie so that len(numAggie) will be accurate 
x = 0
while x < numAggie:
    finalAggie = finalAggie.__add__(["*"])
    x += 1

#converting finalAggie into a string and renaming as numAggie
numAggie = "".join(finalAggie)
#conversion to string 
numAggie = str(numAggie)

#highest possible value to start, so decreasing is the only option (will do validation in loop). outside of loop so it doesn't reset
minimumValue = 1000000000

#numAggie - 1 to make sure end values aren't read and range error doesn't occcur
for value in range(len(numAggie)):
    
    #reading user input for aggie positions in line. assue the user will not enter the value in order 
    placeAggies = input("Enter position in line of three Aggies or press \"q\" to quit. ")
    
    #allows user to exit loop
    if placeAggies == "q":
        break
    
    #should perform an implicit type conversion to a list, splits at each space
    positionInLine = placeAggies.split()

    #forcing conversion from str to int before sorting to ensure values are properly sorted as ints, not strs 
    for char in range(len(positionInLine)):
        positionInLine[char] = int(positionInLine[char])

    #sorts each value from least to greatest. so positionInLine[2] = rightAggie, 1 = currAggie, 0 = leftAggie
    #least to greatest b/c greatest to least ignores 0s on 10, 20, 30, etc. 
    positionInLine.sort()
    #print(positionInLine) #tests to make sure list was sorted 
    
    #named frontFrustration b/c smaller values are in front of line and avoids confusion with function name
    frontFrustration = (positionInLine[value] + positionInLine[value + 1]) / 2
    backFrustration = (positionInLine[value] + positionInLine[value - 1]) / 2
    #abs value to ensure positive number 
    areaFrustration = abs(backFrustration - frontFrustration)
    #print(areaFrustration) #testing to make sure the area functions worked and the Aggie values are correct
    
    #if the area is smaller than the minimum, it will replace the minimum until the smallest value is found
    if areaFrustration < minimumValue:
        minimumValue = areaFrustration
    
    print(f'The smallest area of frustration is: {minimumValue:.1f}.')
    
    #increments regardless of if statement
    value += 1