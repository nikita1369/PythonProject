from Person import Person
from Course import Course

class FacultyMember(Person):

    def __init__(self, employeeId, name, address):
        super().__init__(name, address)

        self.employeeId = employeeId
        self.name = name
        self.address = address

        self.courseList = []

    def addCourse(self, course):
        self.courseList.append(course)

    def dropCourse(self, course):
        self.courseList.remove(course)

    def __str__(self):
        return "Employee ID: " + self.employeeId + "\n" + self.courseList + "\n" + super().__str__()