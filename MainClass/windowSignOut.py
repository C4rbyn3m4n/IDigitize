# imports required modules
import tkinter as tk

import windowScan
import dataStudent
from client import client


class windowSignOut():
    def __init__(self, parent):
        # Stores the parent to allow accessing the previous object variables
        self.parent = parent

        # Makes the main frame to store widgets
        self.frameSignOut = tk.Frame(self.parent.master)

        # Makes the label for the sign-in text
        tk.Label(self.frameSignOut, text=self.parent.varSignIn.get()).pack()

        # Makes the entries for the Name and ID (These will be filled by the card scan)
        tk.Entry(self.frameSignOut, text=self.parent.varName, justify="center").pack()
        tk.Entry(self.frameSignOut, text=self.parent.varID, justify="center").pack()

        # Makes a seperate frame for the buttons to be stored on to allow better formatting
        self.frameSignOutButtons = tk.Frame(self.frameSignOut)

        # Makes both Submit and Cancel buttons and assigns their commands
        tk.Button(self.frameSignOutButtons, text="Submit", command=self.commandSubmit).pack(side=tk.LEFT)
        tk.Button(self.frameSignOutButtons, text="Cancel", command=self.commandCancel).pack(side=tk.RIGHT)

        # Binds the enter key to the submit method
        self.parent.master.bind('<Return>', lambda event: self.commandSubmit())

        # Packs both of the frames
        self.frameSignOutButtons.pack()
        self.frameSignOut.pack()

        # Opens a scan window to get card info
        self.ScanWindow = windowScan.windowScan(self)

    def commandSubmit(self):
        student = dataStudent.dataStudent()
        student.setID(self.parent.varID.get())
        student.setName(self.parent.varName.get())

        client().signOut(student)

        self.parent.varID.set("ID")
        self.parent.varName.set("Name")

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


