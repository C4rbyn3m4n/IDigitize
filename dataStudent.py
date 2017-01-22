

class dataStudent():
    def __init__(self, Name="", ID="", Class="", Teacher=""):
        self.setClass(Class)
        self.setTeacher(Teacher)
        self.setID(ID)
        self.setName(Name)

    def setName(self, Name):
        self.Name = Name

    def setID(self, ID):
        self.ID = ID

    def setClass(self, Class):
        self.Class = Class

    def setTeacher(self, Teacher):
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