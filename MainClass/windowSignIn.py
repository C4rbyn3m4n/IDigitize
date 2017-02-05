import tkinter as tk

import windowClassSelect

from MainClass import windowScan


class windowSignIn():
    def __init__(self, parent):
        self.parent = parent

        self.frameSignIn = tk.Frame(self.parent.master)
        tk.Label(self.frameSignIn, text=self.parent.varSignIn.get()).pack()
        tk.Entry(self.frameSignIn, text=self.parent.varName, justify="center").pack()
        tk.Entry(self.frameSignIn, text=self.parent.varID, justify="center").pack()
        self.frameSignInButtons = tk.Frame(self.frameSignIn)
        tk.Button(self.frameSignInButtons, text="Submit", command=self.commandSubmit).pack(side=tk.LEFT)
        tk.Button(self.frameSignInButtons, text="Cancel", command=self.commandCancel).pack(side=tk.RIGHT)
        self.parent.master.bind('<Return>', lambda event: self.commandSubmit())
        self.frameSignInButtons.pack()
        self.frameSignIn.pack()

        self.ScanWindow = windowScan.windowScan(self)

    def commandSubmit(self):
        if self.parent.varID.get() != "ID" and self.parent.varID.get() != "":
            if self.parent.varName.get() != "Name" and self.parent.varName.get() != "":
                self.parent.varFinalID.set(self.parent.varID.get())
                self.parent.varFinalName.set(self.parent.varName.get())
                self.parent.master.unbind('<Return>')

                print(self.parent.varFinalID.get())
                print(self.parent.varFinalName.get())

                self.frameSignIn.pack_forget()
                self.selectTeacherWindow = windowClassSelect.windowClassSelect(self)

    def commandCancel(self):
        # Clear final variables
        self.parent.varFinalID.set("")
        self.parent.varFinalName.set("")
        self.parent.varName.set("Name")
        self.parent.varID.set("ID")

        self.frameSignIn.destroy()
        self.parent.frameMain.pack()

    def readCard(self, cardInfo):
        start = cardInfo.find("^")
        end = cardInfo.find("^", start+1)

        name = cardInfo[start+1: end]
        name = name.replace("/", ", ")
        name = name.rstrip()

        end = cardInfo.find("?", end)
        id = cardInfo[end-4:end]

        self.parent.varID.set(id)
        self.parent.varName.set(name)


