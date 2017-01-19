

class dataStudent():
    def __init__(self, name, ID, Class, Teacher):
        self.Name = name
        self.ID = ID
        self.Class = Class
        self.Teacher = Teacher

    def getName(self):
        return self.Name

    def getID(self):
        return self.ID

    def getClass(self):
        return self.Class

    def getTeacher(self):
        return self.Teacher

    def __str__(self):
        return "$%$%" + self.Name + "::" + self.ID + "::" + self.Class + "::" + self.Teacher + "%$%$"

    def toString(self):
        return "$%$%" + self.Name + "::" + self.ID + "::" + self.Class + "::" + self.Teacher + "%$%$"