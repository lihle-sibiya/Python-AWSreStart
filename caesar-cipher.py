#Creating a user-defined function
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
    
    #Call the function
alphabet= "ABC"
result = getDoubleAlphabet(alphabet)
print(result)