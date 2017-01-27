

class Tutor():
    def __init__(self, name=""):
        self.setName(name)
        self.assignedStudents = []

    def __str__(self):
        return self.name

    def setName(self, name):
        self.name = name

    def addStudent(self, student):
        self.assignedStudents.append(student)

    def addStudentArray(self, arrayStudents):
        for student in arrayStudents:
            self.assignedStudents.appent(student)

