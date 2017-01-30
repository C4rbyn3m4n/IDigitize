import tkinter as tk
import serverThread
import queue
import requests
from dataTutor import *

class windowListenMain():
    def __init__(self, parent):
        self.parent = parent
        self.students = []
        self.backUpStudents = []
        self.arrayClassTeachers = []
        self.tutors = []
        self.queueServer = queue.Queue()
        self.queueStatus = queue.Queue()
        self.old = ""

        self.parent.protocol('WM_DELETE_WINDOW', self.askForShutDown)

        self.frameMain = tk.Frame(parent)
        self.varStatus = tk.StringVar(self.frameMain)
        self.varListStudents = tk.StringVar(self.frameMain)
        self.varStatus.set("Status: .....")
        tk.Label(self.frameMain, textvariable=self.varStatus, font=("Times New Roman", 10, "bold")).pack()
        self.frameInfo = tk.Frame(self.frameMain)

        self.frameScrollBox = tk.Frame(self.frameInfo)
        tk.Label(self.frameScrollBox, text="Pending Students").pack()
        self.scrollStudents = tk.Scrollbar(self.frameScrollBox)
        self.scrollStudents.pack(side=tk.RIGHT, fill=tk.Y)
        self.listStudents = tk.Listbox(self.frameScrollBox, width=40, yscrollcommand=self.scrollStudents.set, exportselection=0, selectmode=tk.EXTENDED)
        self.listStudents.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollStudents.config(command=self.listStudents.yview)

        self.frameTutorBox = tk.Frame(self.frameInfo)
        tk.Label(self.frameTutorBox, text="Tutors").pack()
        self.scrollTutors = tk.Scrollbar(self.frameTutorBox)
        self.scrollTutors.pack(side=tk.RIGHT, fill=tk.Y)
        self.listTutors = tk.Listbox(self.frameTutorBox, yscrollcommand=self.scrollTutors.set, exportselection=0)
        self.listTutors.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollTutors.config(command=self.listTutors.yview)

        self.frameButtons = tk.Frame(self.frameInfo)
        tk.Button(self.frameButtons, text="Assign Tutor", width=19, command=self.commandAssignTutor).pack()
        tk.Button(self.frameButtons, text="View Students", width=19, command=self.StudentsSignedIn).pack()
        tk.Button(self.frameButtons, text="Shutdown Server", width=19, command=self.askForShutDown).pack()

        self.frameScrollBox.grid(column=0, row=0)
        self.frameTutorBox.grid(column=1, row=0)
        self.frameButtons.grid(column=2, row=0, sticky=tk.EW)
        self.frameInfo.pack()

        self.frameAssignedTutors = tk.Frame(self.frameMain)
        tk.Label(self.frameAssignedTutors, text="Assigned Tutors").pack()
        self.scrollAssignedTutors = tk.Scrollbar(self.frameAssignedTutors)
        self.scrollAssignedTutors.pack(side=tk.RIGHT, fill=tk.Y)
        self.listAssignedTutors = tk.Listbox(self.frameAssignedTutors, yscrollcommand=self.scrollAssignedTutors.set)
        self.listAssignedTutors.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollAssignedTutors.config(command=self.listAssignedTutors.yview)

        self.frameStudentInfo = tk.Frame(self.frameMain)
        tk.Label(self.frameStudentInfo, text="Students").pack()
        # tk.Label(self.frameStudentInfo, textvariable=self.varListStudents).pack()
        self.scrollTutorStudents = tk.Scrollbar(self.frameStudentInfo)
        self.scrollTutorStudents.pack(side=tk.RIGHT, fill=tk.Y)
        self.listTutorStudents = tk.Listbox(self.frameStudentInfo, width=65, yscrollcommand=self.scrollTutorStudents.set)
        self.listTutorStudents.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollAssignedTutors.config(command=self.listTutorStudents.yview)

        self.frameAssignedTutors.pack(side=tk.LEFT)
        self.frameStudentInfo.pack()
        self.frameMain.pack()

        self.addTutors()
        self.varStatus.set("Status: Starting Server...")
        serverThread.serverThread(self.queueServer, self.queueStatus, self).start()
        self.varStatus.set("Status: Server Started")
        self.frameMain.after(1, self.checkQueue)
        self.frameMain.after(2, self.checkStatusQueue)
        self.frameMain.after(3, self.checkTutorList)
        self.parent.bind('<Return>', self.testSelection)

        self.updateClassesAndTutors()

    def checkQueue(self):
        try:
            # print("Size before pull:", self.queueServer.qsize())
            msg = self.queueServer.get_nowait()
            # print("Size after pull:", self.queueServer.qsize())
            if msg == "STUDENT":
                msg = self.queueServer.get()
                self.addStudent(msg)
            elif msg == "SIGNOUT":
                msg = self.queueServer.get()
                self.signOutStudent(msg)
        except queue.Empty:
            pass
        self.frameMain.after(100, self.checkQueue)

    def checkStatusQueue(self):
        try:
            msg = self.queueStatus.get_nowait()
            self.varStatus.set(msg)
        except queue.Empty:
            pass
        self.frameMain.after(100, self.checkStatusQueue)

    def checkTutorList(self):
        if len(self.listAssignedTutors.curselection()) > 0 and self.listAssignedTutors.curselection() != self.old:
            self.old = self.listAssignedTutors.curselection()
            sel = self.listAssignedTutors.get(self.listAssignedTutors.curselection())
            self.listTutorStudents.delete(0, tk.END)
            for i, tutor in enumerate(self.tutors):
                if str(tutor) == sel:
                    selectedTutor = self.tutors[i]
            for i in selectedTutor.assignedStudents:
                self.listTutorStudents.insert(tk.END, i.Class + "- " + str(i))
        self.frameMain.after(100, self.checkTutorList)

    def addTutors(self):
        for tutor in self.tutors:
            self.listTutors.insert(tk.END, tutor)

    def addStudent(self, student):
        # self.listStudents.insert(tk.END, student.getName() + "  " + student.getSignIn())
        self.listStudents.insert(tk.END, student.getClass() + "- " + str(student))
        self.students.append(student)

    def getStudentIndex(self, studentString):
        for i, student in enumerate(self.students):
            print("Stored name of student: ", str(student), "\n Compared to\nInputted Student:", studentString)
            if str(student) in studentString:
                return i
        return -500

    def getTutorIndex(self, tutorString):
        for i, tutor in enumerate(self.tutors):
            if str(tutor) == tutorString:
                return i
        return -500

    def getSelectedStudents(self):
        students = []
        arrayStudentStrings = []
        for i in self.listStudents.curselection():
            arrayStudentStrings.append(self.listStudents.get(i))
        arrayStudentIndex = []
        for stringStudent in arrayStudentStrings:
            arrayStudentIndex.append(self.getStudentIndex(stringStudent))
        for intStudentIndex in arrayStudentIndex:
            students.append(self.students[intStudentIndex])
        return students

    def getSelectedTutor(self):
        return self.tutors[self.getTutorIndex(self.listTutors.get(self.listTutors.curselection()))]

    def commandAssignTutor(self, *args):
        print("Selected Students: ", self.getSelectedStudents())
        if len(self.getSelectedTutor().assignedStudents) == 0:
            self.listAssignedTutors.insert(tk.END, self.getSelectedTutor())
        self.getSelectedTutor().addStudentArray(self.getSelectedStudents())
        print("\nCurrent Selection: ", self.listStudents.curselection())
        j = 0
        for i in self.listStudents.curselection():
            print("Iteration: ", i)
            self.listStudents.delete(i - j)
            j += 1

    def signOutStudent(self, student):
        for i, stu in enumerate(self.students):
            if student in str(stu):
                self.students[i].signOut()
                self.postStudent(self.students[i])
                try:
                    tutor = self.students[i].getTutor()
                    self.students[i].getTutor().assignedStudents.remove(self.students[i])
                    if tutor.assignedStudents == []:
                        l = self.listAssignedTutors.get(0, tk.END)
                        for ii, tut in enumerate(l):
                            if tut == str(tutor):
                                self.listAssignedTutors.delete(ii)
                except Exception as e:
                    print(e)
                    list = self.listStudents.get(0, tk.END)
                    print(list)
                    for ii, stu2 in enumerate(list):
                        if student in stu2:
                            self.listStudents.delete(ii)
                print(self.listTutorStudents.get(0, tk.END))
                for jjj, iii in enumerate(self.listTutorStudents.get(0, tk.END)):
                    print("III: {}     jjj: {}".format(iii, jjj))
                    print("String Student: ", str(student))
                    if str(student) in iii:
                        self.listTutorStudents.delete(jjj)
                self.backUpStudents.append(self.students[i])
                self.students.remove(self.students[i])
                print("Students Array: ", self.students)
                print("Backup students: ", self.backUpStudents)

        print("Signout: " + student)

    def postStudent(self, student):

        htmlLink = "https://docs.google.com/forms/d/e/1FAIpQLSfFjNquxPle7okMntGlut45qzzcQhCUiRIlLns61fB2g3R_og/formResponse"
        entryLocation = ["654751164", "463571797", "2140010094", "1770277963", "995158690", "343862984", "1896892163"]
        data = {}

        data["entry." + entryLocation[0]] = student.getName()
        data["entry." + entryLocation[1]] = student.getID()
        data["entry." + entryLocation[2]] = student.getClass()
        data["entry." + entryLocation[3]] = student.getTeacher()
        data["entry." + entryLocation[4]] = student.getSignIn()
        data["entry." + entryLocation[5]] = student.getSignOut()
        data["entry." + entryLocation[6]] = student.getTutor()
        data["submit"] = "Submit"

        requests.post(htmlLink, data=data)

    def testSelection(self, *args):
        print(self.listStudents.curselection())
        arrayStudentStrings = []
        for i in self.listStudents.curselection():
            arrayStudentStrings.append(self.listStudents.get(i))
            print("Grabbing student with list index of: ", i)
            print("Array of grabbed student strings:    ", str(arrayStudentStrings))
        arrayStudentIndex = []
        for stringStudent in arrayStudentStrings:
            arrayStudentIndex.append(self.getStudentIndex(stringStudent))
            print("Array index of student:  ", stringStudent)
            print("Current array of stored student indexes to check:    ", str(arrayStudentIndex))
        for intStudentIndex in arrayStudentIndex:
            print("Index to check for student:", intStudentIndex)
            print("Stored at index %d is: \n" % intStudentIndex, self.students[intStudentIndex].toString())

        print(self.listTutors.get(self.listTutors.curselection()))

        # print("Selected student:\n", self.getSelectedStudent().toString())

    def updateClassesAndTutors(self):
        teachersHTML = "https://raw.githubusercontent.com/C4rbyn3m4n/IDigitize/master/TeacherTutorInfo/Teachers.txt"
        tutorsHTML = "https://raw.githubusercontent.com/C4rbyn3m4n/IDigitize/master/TeacherTutorInfo/Tutors.txt"

        info = []

        teacherData = requests.get(teachersHTML).text
        lines = teacherData.split('\n')

        for line in lines:
            if "" == line:
                self.arrayClassTeachers.append(info)
                info = []
            else:
                info.append(line)

        TutorData= requests.get(tutorsHTML).text
        lines = TutorData.split('\n')

        for line in lines:
            if line != "":
                self.tutors.append(Tutor(line))
                self.listTutors.insert(tk.END, line)

    def askForShutDown(self, *args):
        # creates window
        self.shutdownTK = tk.Tk()
        self.shutdownTK.resizable(0, 0)

        # set window title
        self.shutdownTK.title("Shutdown")
        self.shutdownTK.lift()
        self.shutdownTK.attributes("-topmost", True)
        self.shutdownTK.after(1, lambda: self.shutdownTK.focus_force())


        # makes a frame on tk window
        self.shutdownFrame = tk.Frame(self.shutdownTK)


        # makes lable
        self.labelShutDown = tk.Label(self.shutdownFrame, text="Are you sure you want to shutdown?")
        self.labelShutDown.pack()

        #makes buttons
        self.frameButtons = tk.Frame(self.shutdownFrame)
        self.buttonOkay = tk.Button(self.frameButtons, text="OK", command=self.commandShutdown, height=3, width=10)
        self.buttonOkay.pack(side=tk.LEFT)
        self.shutdownTK.bind('<Return>', lambda event: self.commandShutdown())
        self.frameButtons.pack()
        tk.Button(self.frameButtons, text="Cancel", height=3, width=10, command=lambda: self.shutdownTK.destroy()).pack(side=tk.RIGHT)
        self.shutdownFrame.pack()

        self.shutdownTK.mainloop()

    def commandShutdown(self):
        for i, stu in enumerate(self.students):
            self.postStudent(self.students[i])
        self.shutdownTK.destroy()
        self.parent.destroy()

    def StudentsSignedIn(self):
        print("hi")
        # creates window
        self.studentsLeftTK = tk.Tk()
        self.studentsLeftTK.resizable(0, 0)

        # set window title
        self.studentsLeftTK.title("Shutdown")
        self.studentsLeftTK.lift()
        self.studentsLeftTK.attributes("-topmost", True)
        self.studentsLeftTK.after(1, lambda: self.studentsLeftTK.focus_force())

        self.listStudents = tk.Listbox(self.studentsLeftTK, width=40, yscrollcommand=self.scrollStudents.set, exportselection=0, selectmode=tk.EXTENDED)
        self.listStudents.pack(side=tk.LEFT, fill=tk.BOTH)


        for i, stu in enumerate(self.students):
            self.listStudents.insert(tk.END, self.students[i].getName())

        # makes a frame on tk window
        self.studentsLeftFrame = tk.Frame(self.studentsLeftTK)
        self.studentsLeftFrame.pack()

        self.studentsLeftTK.mainloop()
