# Michael Vu
# Student ID: 010845718

import csv
import datetime

from HashTable import ChainingHashTable
from Package import Package
from Truck import Truck


# Function to load each package into hash table
def loadPackageData(filename, packageHashTable):
    with open(filename) as packages:
        packageData = csv.reader(packages)
        for package in packageData:
            pID = int(package[0])
            pAddress = (package[1])
            pCity = (package[2])
            pState = (package[3])
            pZipcode = (package[4])
            pDeadline = (package[5])
            pWeight = (package[6])
            pStatus = "At Hub"

            # Package object
            p = Package(pID, pAddress, pCity, pState, pZipcode, pDeadline, pWeight, pStatus)

            # Insert package into hash table
            packageHashTable.insert(pID, p)


# Hash table instance
packageHashTable = ChainingHashTable()

# Load packages to hash table
loadPackageData("WGUPS_Package_File.csv", packageHashTable)


# Function to load distances into distanceData list
def loadDistanceData(filename):
    distanceData = []
    with open(filename) as distanceCSV:
        distanceReader = csv.reader(distanceCSV)
        for row in distanceReader:
            # Append the row as a list to the distanceData list
            distanceData.append(row)
    return distanceData


# Call loadDistanceData function
distanceData = loadDistanceData('WGUPS_Distance_File.csv')


# Define loadAddressData function
def loadAddressData(filename):
    addressData = []
    with open(filename) as addressCSV:
        addressReader = csv.reader(addressCSV)
        for row in addressReader:
            # Use Dictionary structure to assign each address to a key "address"
            addressInfo = {"address": row[2]}
            addressData.append(addressInfo)
    return addressData


addressData = loadAddressData("Address_File.csv")


# Function to calculate distance between 2 addresses
def distanceBetween(address1, address2):
    # If the next package is at the current address, return 0 to deliver the package
    if address1 == address2:
        return 0.0
    # Find the indices of the addresses in addressData
    index1 = None
    index2 = None

    for idx, addressInfo in enumerate(addressData):
        if addressInfo["address"] == address1:
            index1 = idx
        elif addressInfo["address"] == address2:
            index2 = idx

        # If both indices are found, exit the loop
        if index1 is not None and index2 is not None:
            break

    # Extracts the non-empty indices
    if index1 > index2:
        return float(distanceData[index1][index2])
    else:
        return float(distanceData[index2][index1])


# Initialize first Truck object
# Starting location, mileage, package capacity, package list, depart time
truck1 = Truck(1, "4001 South 700 East", 0.0, 16, [1, 13, 14, 15, 16, 19, 20, 21, 29, 30, 31, 34, 37, 40],
               datetime.timedelta(hours=8))
truck2 = Truck(2, "4001 South 700 East", 0.0, 16, [3, 6, 12, 17, 18, 22, 23, 24, 26, 27, 35, 36, 38, 39],
               datetime.timedelta(hours=9, minutes=5))
truck3 = Truck(3, "4001 South 700 East", 0.0, 16, [2, 4, 5, 7, 8, 9, 10, 11, 25, 28, 32, 33],
               datetime.timedelta(hours=10, minutes=20))

# Update Package #9's address
p9 = packageHashTable.search(9)
p9.address = "410 S State St"
p9.zipcode = "84111"


def truckDeliverPackages(truck):
    # Initialize current location
    currentLocation = truck.location
    # Continue until package list is 0
    while len(truck.packageList) > 0:
        minDistance = 4000
        nextDelivery = None

        for ID in truck.packageList:
            package = packageHashTable.search(ID)
            if package.status != "Delivered":
                distance = distanceBetween(currentLocation, package.address)
                # Update minDistance and next delivery if it is higher than calculated distance
                if distance < minDistance:
                    minDistance = distance
                    nextDelivery = package
                    nextDelivery.truckID = truck.ID

        # Convert the constant speed of 18 MPH to time elapsed
        deliveryTime = datetime.timedelta(hours=minDistance / 18)
        currentLocation = nextDelivery.address
        # Remove recently delivered package
        truck.packageList.remove(nextDelivery.ID)
        # Update total time and mileage
        truck.time += deliveryTime
        truck.mileage += minDistance
        # Set deliveryTime and departureTime for the package
        nextDelivery.deliveryTime = truck.time
        nextDelivery.departureTime = truck.departTime


truckDeliverPackages(truck1)
truckDeliverPackages(truck2)
truckDeliverPackages(truck3)

totalMileage = truck1.mileage + truck2.mileage + truck3.mileage
print(f"\nTotal mileage to deliver all packages: {round(totalMileage, 2)}")


# Start of CLI
# Function to take user input as time
def userInput():
    userTimeChoice = input("Please enter a time to check (HH:MM): ")
    (h, m) = userTimeChoice.split(":")
    convertUserTime = datetime.timedelta(hours=int(h), minutes=int(m))
    return convertUserTime


while True:
    print("\nMenu:")
    print("1. Get Single Package Status with Time")
    print("2. Get All Package Statuses with Time")
    print("3. Exit")
    userChoice = input("Please select an option (1-3): ")

    if userChoice == "1":
        searchPackageID = int(input("Enter the Package ID: "))
        time = userInput()
        package = packageHashTable.search(searchPackageID)
        package.updateStatus(time)
        if package.ID == 9 and time > datetime.timedelta(hours=10, minutes=20):
            p9.address = "410 S State St"
            p9.zipcode = "84111"
        else:
            p9.address = "300 State St"
            p9.zipcode = "84103"
        if package.deliveryTime <= time:
            print(
                f"Package ID: {package.ID}, Address: {package.address}, {package.city}, {package.state}, {package.zipcode}, Deadline: {package.deadline}, Weight: {package.weight}   Status: {package.status} at time {package.deliveryTime} by Truck {package.truckID}")
            print(f"\nTotal mileage to deliver all packages: {round(totalMileage, 2)}")
        else:
            print(
                f"Package ID: {package.ID}, Address: {package.address}, {package.city}, {package.state}, {package.zipcode}, Deadline: {package.deadline}, Weight: {package.weight}   Status: {package.status} on Truck {package.truckID}")
            print(f"\nTotal mileage to deliver all packages: {round(totalMileage, 2)}")

    elif userChoice == "2":

        time = userInput()
        for packageID in range(1, 41):
            package = packageHashTable.search(packageID)
            package.updateStatus(time)
            if package.ID == 9 and time > datetime.timedelta(hours=10, minutes=20):
                p9.address = "410 S State St"
                p9.zipcode = "84111"
            else:
                p9.address = "300 State St"
                p9.zipcode = "84103"
            if package.deliveryTime <= time:
                print(
                    f"Package ID: {package.ID}, Address: {package.address}, {package.city}, {package.state}, {package.zipcode}, Deadline: {package.deadline}, Weight: {package.weight}  Departure Time:{package.departureTime} Status: {package.status} at time {package.deliveryTime} by Truck {package.truckID}")
            else:
                print(
                    f"Package ID: {package.ID}, Address: {package.address}, {package.city}, {package.state}, {package.zipcode}, Deadline: {package.deadline}, Weight: {package.weight}  Departure Time: {package.departureTime} Status: {package.status} on Truck {package.truckID}")
        print(f"\nTotal mileage to deliver all packages: {round(totalMileage, 2)}")

    elif userChoice == "3":
        exit()
