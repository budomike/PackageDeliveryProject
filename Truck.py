# Create Truck class
class Truck:

    def __init__(self, ID, location, mileage, packages, packageList, departTime):
        self.ID = ID
        self.location = location
        self.mileage = mileage
        self.packages = packages
        self.packageList = packageList
        self.departTime = departTime
        self.time = departTime

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s" % (self.ID, self.location, self.mileage, self.packages, self.packageList, self.departTime)
