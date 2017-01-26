import tkinter as tk
import serverThread
import queue

class windowListenMain():
    def __init__(self, parent):
        self.parent = parent
        self.students = []
        self.tutors = ["Tutor 1", "Tutor 2", "Tutor 3", "Tutor 4"]
        self.queueServer = queue.Queue()


        self.frameMain = tk.Frame(parent)
        self.varStatus = tk.StringVar(self.frameMain)
        self.varStatus.set(".....")
        tk.Label(self.frameMain, textvariable=self.varStatus).pack()
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
        tk.Button(self.frameButtons, text="Assign Tutor").pack()

        self.frameScrollBox.grid(column=0, row=0)
        self.frameTutorBox.grid(column=1, row=0)
        self.frameButtons.grid(column=2, row=0)
        self.frameInfo.pack()
        self.frameMain.pack()

        self.addTutors()
        self.varStatus.set("Starting Server...")
        serverThread.serverThread(self.queueServer).start()
        self.varStatus.set("Server Started")
        self.frameMain.after(1, self.checkQueue)
        self.parent.bind('<Return>', self.testSelection)


    def checkQueue(self):
        try:
            # print("Size before pull:", self.queueServer.qsize())
            msg = self.queueServer.get_nowait()
            # print("Size after pull:", self.queueServer.qsize())
            print(msg)
            self.addStudent(msg)
            self.queueServer.qsize()
        except queue.Empty:
            pass
        self.frameMain.after(100, self.checkQueue)

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

    def getSelectedStudent(self):
        return self.students[self.getStudentIndex(self.listStudents.get(self.listStudents.curselection()))]

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

        # print("Selected student:\n", self.getSelectedStudent().toString())
