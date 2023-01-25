### 3 rules of recursion ##
# establish a base case
# incriment or decriment your recursion towards your base case 
# you must use recursion, not a loop

#defining reference variables
encodeDic = {}
textMsg = ""
encodeMsg = ""

#total six reference variables
#decodeMsg and encodeMsg are not restated, eliminates clutter in code

encodeDic = {" ": "r", "a": "#", "b": "$", "c": "@", "d": "*", "e": "!", "f": ")",
            "g": "(", "h": "&", "i": "{", "j": "}", "k": ":", "l": "^", "m": "'",
            "n": "?", "o": ">", "p": "<", "q": "+", "r": "|", "s": "~", "t": "`",
            "u": "-", "v": "%", "w": "8", "x": "5", "y": "=", "z": "0"}
textMsg = str(input("Enter message to encode: ")).lower() #.lower prevents runtime errors if caps are used

for i in textMsg:
    encodeMsg += encodeDic.get(i)
print(f'Encoded message: {encodeMsg}\n') #better spacing for changing between encoding/decoding
#for loop will replace each character by creating a new string with each iteration 

#writing a recursive function to decode the inputed encoded message, input will be read following function def
print(encodeDic)
print(encodeDic.keys())
print(encodeDic.values())