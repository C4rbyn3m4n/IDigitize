import tkinter as tk

class windowAssignClass():
    def __init__(self, student, parent):
        self.parent = parent
        self.student = student
        self.main = tk.Tk()
        self.main.title("Select Class")
        frameMain = tk.Frame(self.main)
        self.Class = tk.StringVar(frameMain)
        self.Class.set("Class")

        tk.Label(frameMain, text="Please enter the class for " + self.student.getName()).pack(side=tk.TOP)
        tk.Entry(frameMain, text=self.Class).pack()
        tk.Button(frameMain, text="Okay", command=self.commandOkay).pack()

        self.main.bind('<Return>', lambda *event: self.commandOkay())

        frameMain.pack()
        self.main.mainloop()

    def commandOkay(self):
        print("The new class is: ", self.Class.get())
        self.student.setClass(self.Class.get())
        self.main.destroy()
        self.parent.commandAssignTutor()

