print("Hello, World")
print("Python has three numeric types: int, float, and complex")

myValue=1
print(myValue)

print(type(myValue))

print(str(myValue) + " is of the data type " + str(type(myValue)))

print("# # # # # # # #       #     #    #")
# Float Data type
myValue1=3.14
print(myValue1)
print(str(myValue1) + " is of the data type " + str(type(myValue1)))

print("# # # # # # # #       #     #    #")
# Complex Data type

myValue2=5j
print(type(myValue2))
print(str(myValue2) + " is of the data type " + str(type(myValue2)))


print("# # # # # # # #       #     #    #")
# Boolean Data type

myValue3=True
print(myValue3)
print(type(myValue3))
print(str(myValue3) + " is of the data type " + str(type(myValue3)))


print("# # # # # # # #       #     #    #")
# String Data type

myString = "This is a string."
print(myString)
print(type(myString))
#Str- return value into a string
print(myString + " is of the data type " + str(type(myString)))

print("# # # # # # # #       #     #    #")
#Concanate
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

#name = input("What is your name? ")
#print(name)

print("# # # # # # # #       #     #    #")
#Lists
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

print("# # # # # # # #       #     #    #")
#Lists - changing value
myFruitList[2] = "orange"
print(myFruitList)


print("# # # # # # # #       #     #    #")
# Tuple Data type
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

print("# # # # # # # #       #     #    #")
# Dictionary

myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

#access Akua's favorite fruit
print(myFavoriteFruitDictionary["Akua"])
#access Saanvi's favorite fruit
print(myFavoriteFruitDictionary["Saanvi"])
#access Paulo's favorite fruit
print(myFavoriteFruitDictionary["Paulo"])


print("# # # # # # # #       #     #    #")
# mixed-type list