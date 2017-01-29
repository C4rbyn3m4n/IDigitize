import time

class dataStudent():
    def __init__(self, Name="", ID="", Class="", Teacher="", SignIn="", SignOut="", Tutor=""):
        self.setClass(Class)
        self.setTeacher(Teacher)
        self.setID(ID)
        self.setName(Name)
        self.setSignIn(SignIn)
        self.setSignOut(SignOut)
        self.setTutor(Tutor)

    def setName(self, Name):
        self.Name = Name

    def setID(self, ID):
        self.ID = ID

    def setClass(self, Class):
        self.Class = Class

    def setTeacher(self, Teacher):
        self.Teacher = Teacher

    def setSignIn(self, SignIn):
        self.SignIn = SignIn

    def setSignOut(self, SignOut):
        self.SignOut = SignOut

    def signIn(self):
        self.SignIn = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def setTutor(self, tutor):
        self.Tutor = tutor

    def getName(self):
        return self.Name

    def getID(self):
        return self.ID

    def getClass(self):
        return self.Class

    def getTeacher(self):
        return self.Teacher

    def getSignIn(self):
        return self.SignIn

    def getSignOut(self):
        return self.SignOut

    def getTutor(self):
        return self.Tutor

    def __str__(self):
        # return "$%$%" + self.Name + "::" + self.ID + "::" + self.Class + "::" + self.Teacher + "%$%$"
        return self.Name + " : " + self.ID

    def toString(self):
        temp = "Name: " + self.Name + "\n" \
               "    ID: " + self.ID + "\n" \
               "    Class: " + self.Class + "\n" \
               "    Teacher: " + self.Teacher + "\n" \
               "    SignIn Time: " + self.SignIn + "\n" \
               "    SignOut Time: " + self.SignOut + "\n"
        return temp

    def signOut(self):
        self.SignOut = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
