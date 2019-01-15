class Course:

    def __init__(self, courseIdentifier, courseTitle):
        self.courseIdentifier = courseIdentifier
        self.courseTitle = courseTitle

    def __str__(self):
        return self.courseIdentifier + ": " + self.courseTitle