import tkinter as tk
import serverThread
import queue
import requests
from dataTutor import *

class windowListenMain():
    def __init__(self, parent):
        self.parent = parent
        self.students = []
        self.arrayClassTeachers = []
        self.tutors = []
        self.queueServer = queue.Queue()
        self.queueStatus = queue.Queue()


        self.frameMain = tk.Frame(parent)
        self.varStatus = tk.StringVar(self.frameMain)
        self.varStatus.set("Status: .....")
        tk.Label(self.frameMain, textvariable=self.varStatus, font=("Times New Roman", 10, "bold")).pack()
        self.frameInfo = tk.Frame(self.frameMain)

        self.frameScrollBox = tk.Frame(self.frameInfo)
        tk.Label(self.frameScrollBox, text="Pending Students").pack()
        self.scrollStudents = tk.Scrollbar(self.frameScrollBox)
        self.scrollStudents.pack(side=tk.RIGHT, fill=tk.Y)
        self.listStudents = tk.Listbox(self.frameScrollBox, yscrollcommand=self.scrollStudents.set, selectmode=tk.EXTENDED)
        self.listStudents.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollStudents.config(command=self.listStudents.yview)

        self.frameTutorBox = tk.Frame(self.frameInfo)
        tk.Label(self.frameTutorBox, text="Tutors").pack()
        self.scrollTutors = tk.Scrollbar(self.frameTutorBox)
        self.scrollTutors.pack(side=tk.RIGHT, fill=tk.Y)
        self.listTutors = tk.Listbox(self.frameTutorBox, yscrollcommand=self.scrollTutors.set)
        self.listTutors.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollTutors.config(command=self.listTutors.yview)

        self.frameButtons = tk.Frame(self.frameInfo)
        tk.Button(self.frameButtons, text="Assign Tutor", width=19).pack(fill="x")

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

        self.frameAssignedTutors.pack()
        self.frameMain.pack()

        self.addTutors()
        self.varStatus.set("Status: Starting Server...")
        serverThread.serverThread(self.queueServer, self.queueStatus, self).start()
        self.varStatus.set("Status: Server Started")
        self.frameMain.after(1, self.checkQueue)
        self.frameMain.after(2, self.checkStatusQueue)
        self.parent.bind('<Return>', self.testSelection)

        self.updateClassesAndTutors()

    def checkQueue(self):
        try:
            # print("Size before pull:", self.queueServer.qsize())
            msg = self.queueServer.get_nowait()
            # print("Size after pull:", self.queueServer.qsize())
            self.addStudent(msg)
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

    def addTutors(self):
        for tutor in self.tutors:
            self.listTutors.insert(tk.END, tutor)

    def addStudent(self, student):
        # self.listStudents.insert(tk.END, student.getName() + "  " + student.getSignIn())
        self.listStudents.insert(tk.END, student)
        self.students.append(student)

    def getStudentIndex(self, studentString):
        for i, student in enumerate(self.students):
            print("Stored name of student: ", str(student), "\n Compared to\nInputted Student:", studentString)
            if str(student) == studentString:
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

    def commandAssignTutor(self):
        self.getSelectedTutor().addStudentArray(self.getSelectedStudents())
        for i in self.listStudents.curselection():
            self.listStudents.delete(i)

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
