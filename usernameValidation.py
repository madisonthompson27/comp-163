def CodelandUsernameValidation(strParam):

    #initializing reference var 
    marker = True
    
    #checking string length (step 1)
    if len(strParam) in range(4, 26):
        marker = True
    else:
        marker = False
    
    if marker == True:
    #verifying only letters, numbers, and underscores
        tempVar = str(strParam).replace("_","")
        if tempVar.isalnum():
            marker = True
        else:
            marker = False

    if marker == True:
        #verifying starts with str and doesn't end with underscore (steps 2 and 4)
        if (strParam[0].isdigit() == False) and (strParam[-1] != "_") and (strParam[0] != "_"):
            marker = True
        else:
            marker = False
    
    
    print(marker)

# keep this function call here 
print(CodelandUsernameValidation(input()))