"""
Madison Thompson
10/05/2022
COMP 163-001
This program takes a message and uses a combination of dictionary methods, for loops, and recursive functions to either encode or decode. 
Encoding and decoding reference the same dictionary, the decoding dictionary is just reversed. values inputed must be in dict. 
"""

#defining reference variables
encodeDic = {}
textMsg = ""
encodeMsg = ""

#defining encodeDic, this dic is the one on the blackboard assignment
encodeDic = {" ": "^", "a": "&", "b": "$", "c": "!", "d": ".", "e": "3", "f": "?", "g": "*", "h": "+",
             "i": ":", "j": "8", "k": "@", "l": "w", "m": "2", "n": "`", "o": "6", "p": "f", "q": "<",
             "r": ">", "s": "/", "t": "x", "u": "0", "v": "u", "w": "s", "x": "[", "y": "{", "z": "("}
textMsg = str(input("Enter message to encode: ")).lower() #.lower prevents runtime errors if caps are used

for i in textMsg:
    encodeMsg += encodeDic.get(i)
print(f'Encoded message: {encodeMsg}\n') #better spacing for changing between encoding/decoding
#for loop will replace each character by creating a new string with each iteration 


#writing a recursive function to decode the inputed encoded message, input will be read following function def
def decoded_message(secondMsg, finalMsg=""):
    #reversing values of the encoded dictionary
    decodeValues = list(encodeDic.keys())
    decodeKeys= list(encodeDic.values())
    
    #using numeric iteration so that strings are protected from accidental mutation
    count = 0
    char = secondMsg[count]
    
    #if the character from the string is present, find the value from decodeValues and add the decoded value to finalMsg
        #some bugs were present with this statement, so for safety the test version is currently running
    if char in decodeKeys:
        tempVar = decodeKeys.index(char)
        finalMsg = decodeValues[tempVar]
        print(finalMsg, end="") #used for testing to make sure final message works. concatenates as a string. 
        
        #third value must be included as a count, so that duplicate letters aren't all omitted
        secondMsg = secondMsg.replace(char, "", 1)
        
    #using a base value to determine if recursion will occur
    if count != len(secondMsg):
        decoded_message(secondMsg, finalMsg)
    
   
#taking user input value. lower ensures that alpha characters are in the correct case.
secondMsg = str(input("Enter message to be decoded: ")).lower()

#call function and assign string ending. would be more functional if finalMsg was an adaptive variable and f' could be utilized. 
print("Decoded message:", end=" ")
decoded_message(secondMsg)