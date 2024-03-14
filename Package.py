# Create Package class
class Package:
    def __init__(self, ID, address, city, state, zipcode, deadline, weight, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.departureTime = None
        self.deliveryTime = None
        self.truckID = None

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zipcode,
                                                   self.deadline, self.weight, self.status, self.truckID
                                                   )

    # Updates status based on time entered
    def updateStatus(self, statusTime):
        if self.deliveryTime < statusTime:
            self.status = "Delivered"
        elif self.departureTime > statusTime:
            self.status = "At Hub"
        else:
            self.status = "En Route"
        return self.status

