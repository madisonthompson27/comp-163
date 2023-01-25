'''
Madison Thompson
9/29/2022
COMP 163-001
This program uses the random module, for loops, string joining to ensure that a for loop iterates through randomly generated numbers
in the range random.randint(-1000000000, 1000000001) the number of times that the user inputed. It then finds the lowest area of 
frustration, or smallest value between consecutive randomly assigned values. It outputs the smallest area of frustration following execution. 
'''
#importing module to assign aggies with a position in line in the specified range
import random

#initializing reference variables
positionInLine = []
finalAggie = []
x = 0

#size of line, will be used to determine how many iterations are ran in the for loop
numAggie = int(input("Enter number of Aggies in line: "))

#assigns characters to finalAggie so that len(numAggie) will be accurate 
while x < numAggie:
    finalAggie = finalAggie.__add__(["*"])
    x += 1

#converting finalAggie into a string and renaming as numAggie
numAggie = "".join(finalAggie)
#conversion to string 
numAggie = str(numAggie)

#highest possible value to start, so decreasing is the only option. validation done by range in line 18. outside of loop so it doesn't reset.
minimumValue = 1000000000

#num aggie is a str and len of the string is used to determine iterations
for value in range(len(numAggie)):
    
    #randomly assigns three integer values to the positionInLine list for adjacent indexes
    for i in range(0, 3):
        i = random.randint(-1000000000, 1000000001)
        positionInLine = positionInLine.__add__([i])
        i += 1

    #positionInLine must be converted into ints before it is sorted
    for char in range(len(positionInLine)):
        positionInLine[char] = int(positionInLine[char])

    #sorting from least to greatest to ensure left area of frustration is smallest 
    positionInLine.sort()

    #named frontFrustration b/c smaller values are in front of line and avoids confusion with function name
    frontFrustration = (positionInLine[value] + positionInLine[value + 1]) / 2
    backFrustration = (positionInLine[value] + positionInLine[value - 1]) / 2
    #abs value to ensure positive number 
    areaFrustration = abs(backFrustration - frontFrustration)
    #print(areaFrustration) #testing to make sure the area functions worked and the Aggie values are correct
    
    #if the area is smaller than the minimum, it will replace the minimum until the smallest value is found
    if areaFrustration < minimumValue:
        minimumValue = areaFrustration
        
    #increments regardless of if statement
    value += 1

print(f'The smallest area of frustration is: {areaFrustration:.1f}.')