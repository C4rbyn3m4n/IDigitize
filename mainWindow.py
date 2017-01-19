import tkinter as tk
import windowSignOut, windowSignIn

class mainWindow():
    def __init__(self, master):
        # make parent accessible for all methods
        self.master = master

        # create sign-in and sign-out buttons
        self.frameMain = tk.Frame(self.master)

        self.geom = '200x200+0+0'
        self.master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))

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

    def readCardData(self, cardInfo):
        # self.swipe.destroy()
        # TODO: Readcard data
        print(cardInfo)
        self.swipe.destroy()

    def getSwipe(self):
        # creates window
        self.swipe = tk.Tk()
        # set window title
        self.swipe.title("Input box")
        self.swipe.lift()
        self.swipe.attributes("-topmost", True)
        self.swipe.after(1, lambda: self.swipe.focus_force())

        # makes a frame on tk window
        self.mframe = tk.Frame(self.swipe)
        # makes string variable that can be set
        self.var = tk.StringVar(self.mframe)
        self.CardLabel = tk.Label(self.mframe, text="Scan your card")
        self.CardLabel.pack()
        self.mEntry = tk.Entry(self.mframe, text=self.var)
        self.mEntry.pack()
        self.mEntry.focus()

        self.frameButtons = tk.Frame(self.mframe)
        self.buttonOkay = tk.Button(self.frameButtons, text="OK", command=lambda: self.readCardData(self.var.get()))
        self.buttonOkay.pack(side=tk.LEFT)
        self.swipe.bind('<Return>', lambda event: self.readCardData(self.var.get()))

        tk.Button(self.frameButtons, text="Cancel", command=lambda: self.swipe.destroy()).pack(side=tk.RIGHT)

        self.frameButtons.pack()
        self.mframe.pack()
        self.swipe.mainloop()

        return True