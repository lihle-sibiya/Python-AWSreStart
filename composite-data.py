# Composite Data type

import csv
import copy

#define a dictionary
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

#Use a for loop to iterate over the initial keys and values of the dictionary
for key, value in myVehicle.items():
    print("{} : {}".format(key,value))
    
#Define an empty list to hold the car inventory
myInventoryList = []

#keeps a file open while you read data: keeps a file open while you read data
with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    lineCount = 0  
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  #new storage boxes are created in memory to store the new tabular data that is being read
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')
    
    
   # Print the car inventory
for myCarProperties in myInventoryList:  # This is the outer for loop
    for key, value in myCarProperties.items():  # This is the inner for loop, indented
        print("{} : {}".format(key, value))  # This is part of the inner for loop, further indented
    print("-----")  # This line is also part of the outer for loop but not the inner loop