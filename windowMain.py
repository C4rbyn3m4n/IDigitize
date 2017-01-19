import tkinter as tk
import windowSignOut, windowSignIn

class windowMain():
    def __init__(self, master):
        # make parent accessible for all methods
        self.master = master

        # create sign-in and sign-out buttons
        self.frameMain = tk.Frame(self.master)

        self.master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
        self.master.bind('<Escape>', lambda event: self.master.geometry('{}x{}'.format(500, 500)))

        # sign-in and sign-out buttons and pack
        self.buttonSignIn = tk.Button(self.frameMain, height=13, width=55, text="Sign In", command=self.commandSignIn)
        self.buttonSignIn.pack()
        self.buttonSignOut = tk.Button(self.frameMain, height=13, width=55, text="Sign Out", command=self.commandSignOut)
        self.buttonSignOut.pack()

        self.frameMain.pack()

        # Variable Declaration
        self.varSignIn = tk.StringVar(self.frameMain)
        self.varID = tk.StringVar(self.frameMain)
        self.varName = tk.StringVar(self.frameMain)

        self.varFinalName = tk.StringVar(self.frameMain)
        self.varFinalID = tk.StringVar(self.frameMain)

        self.varName.set("Name")
        self.varID.set("ID")
        self.varSignIn.set("Please swipe your student ID card")


    def commandSignIn(self):
        # hides the main class buttons
        self.frameMain.pack_forget()

        self.signinWindow = windowSignIn.windowSignIn(self)

    def commandSignOut(self):
        # set up variables for the Sign out window

        # hide the main class buttons
        self.frameMain.pack_forget()

        self.signoutWindow = windowSignOut.windowSignOut(self)


