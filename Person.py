class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return "Name: " + self.name + "\n" + self.address