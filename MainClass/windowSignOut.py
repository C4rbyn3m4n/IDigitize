import tkinter as tk

import windowScan
import dataStudent
from client import client


class windowSignOut():
    def __init__(self, parent):
        self.parent = parent

        self.frameSignOut = tk.Frame(self.parent.master)
        tk.Label(self.frameSignOut, text=self.parent.varSignIn.get()).pack()
        tk.Entry(self.frameSignOut, text=self.parent.varName, justify="center").pack()
        tk.Entry(self.frameSignOut, text=self.parent.varID, justify="center").pack()
        self.frameSignOutButtons = tk.Frame(self.frameSignOut)
        tk.Button(self.frameSignOutButtons, text="Submit", command=self.commandSubmit).pack(side=tk.LEFT)
        tk.Button(self.frameSignOutButtons, text="Cancel", command=self.commandCancel).pack(side=tk.RIGHT)
        self.parent.master.bind('<Return>', lambda event: self.commandSubmit())
        self.frameSignOutButtons.pack()
        self.frameSignOut.pack()

        self.ScanWindow = windowScan.windowScan(self)

    def commandSubmit(self):
        student = dataStudent.dataStudent()
        student.setID(self.parent.varID.get())
        student.setName(self.parent.varName.get())

        client().signOut(student)




        self.frameSignOut.destroy()
        self.parent.frameMain.pack()

    def commandCancel(self):
        # clear final variables
        self.parent.varFinalID.set("")
        self.parent.varFinalName.set("")
        self.parent.varName.set("Name")
        self.parent.varID.set("ID")

        self.frameSignOut.destroy()
        self.parent.frameMain.pack()

    def readCard(self, cardInfo):
        # self.swipe.destroy()
        # TODO: Readcard data
        print(cardInfo)


