#Exercise 1: Creating a user-defined function
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
    
    #Call the function
alphabet= "ABC"
result = getDoubleAlphabet(alphabet)
print(result)

#Exercise 2: Encrypting a message
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt