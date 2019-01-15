class Address:

    def __init__(self, streetNum, streetName, city, state, country):
        self.streetNum = streetNum
        self.streetName = streetName
        self.city = city
        self.state = state
        self.country = country

    def __str__(self):
        return self.streetNum + " " + self.streetName + "\n" + self.city + ", " + self.state + " " + self.country