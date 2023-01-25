'''
Madison Thompson
9/23/2022
COMP 163-001
This program uses boolean values and while loops to sort randomly generated list values from least to greatest by holding
the smaller value in a temp variable and updating the list index that will read to ensure it is moved to the proper location. 
'''
#importing modules to allow for random generation of ints and a slower runtime for testing
import random 
import time

#initializing reference vairables, with initialization value dependent on type. variables in order of occurance 
sizeList = 0 #int value to determine len(sortValues)
sortValues = [] #list that will be sorted 
needToSwapAnywhere = True #boolean value is true so that the loop runs initially, if no swap occurs the loop fails (sentinel value)
tempVar = 0 #holds smaller value until it can be moved within list
pointer = "" #pointer keeps track of index value within list
#prevPointer = "" secondary temp var used in testing 

#determining number of values that will be in list sortValues by assigning sizeList to a randomint value form the random module
sizeList = random.randint(10,21)

#determining the values of sortValues using a for statement and the random module to ensure any value works in the code
for x in range(sizeList): #will run for every value of sizeList, meaning sortValues will be the len(sizeList)
        x = random.randint(-50,51) #must go to 51 b/c open interval 
        sortValues = sortValues.__add__([x]) #.append does not work with an empty list, x is taken as a list input
            
pointer = 1 #pointer determined
#print(sortValues) can be used during testing or running to see original list, then output

#using an while loop so that repeating takes less code and ensures each value will be sorted (restart at list end)
while needToSwapAnywhere != False:
    if pointer == len(sortValues): #if at the end of the list then check to make sure swapping occurred
        needToSwapAnywhere == False 
        break #backup escape for while loop 
    if sortValues[pointer - 1] > sortValues[pointer]:
        needToSwapAnywhere = True #makes sure that loop repeats by being the opposite of sentinel condition
        #prevPointer = pointer - 1 #secondary variable used in testing, value of prevPointer is stored to protect iterations 
        tempVar = sortValues[pointer] #if the first value is greater than the second, the second needs to become the first 
        sortValues[pointer] = sortValues[pointer - 1]
        sortValues[pointer - 1] = tempVar
        #time.sleep(2) used for testing purposes and slowing algorithim
        pointer = 1 #restarts at index 1 to move a new value 
    else:
        pointer += 1 #ensures incrementation before breaking 
print(sortValues) #final print of value 