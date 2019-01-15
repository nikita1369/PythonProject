from Person import Person
from Course import Course

#The parent class Person of Student must be included in parenthesis
class Student(Person):

    def __init__(self, cinNumber, name, address):
        #Initialize attributes of the parent class
        super().__init__(name, address)

        self.cinNumber = cinNumber
        self.courseList = []

    def addCourse(self, course):
        self.courseList.append(course)

    def dropCourse(self, course):
        self.courseList.remove(course)

    def __str__(self):
        return "CIN number: " + self.cinNumber + "\n" + self.courseList + "\n" + super().__str__()