import tkinter as tk
import windowSignIn
from client import client

from MainClass import windowSignOut


class windowMain():
    def __init__(self, master):
        # make parent accessible for all methods
        self.master = master
        #loads the teacher/class array from the server
        self.loadClassTeachers()

        # create the main frame for the object
        self.frameMain = tk.Frame(self.master)

        # format the window size to fill the screen completely
        self.master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
        # make escape key reduce window size for debugging
        self.master.bind('<Escape>', lambda event: self.master.geometry('{}x{}'.format(500, 500)))
        # binds Control+Shift+t to shutdown the server
        self.master.bind('<Control-T>', lambda event: self.master.destroy())
        # prevents the 'x' button from destroying the window
        self.master.protocol('WM_DELETE_WINDOW', self.doNothing)

        # TODO: Add background image
        # self.imageBackground = tk.PhotoImage("FloridaPolyGray.png")
        # self.labelBackgroundImage = tk.Label(self.frameMain, image=self.imageBackground)
        # self.labelBackgroundImage.place(x=0, y=0, relwidth=1, relheight=1)
        # self.labelBackgroundImage.pack()

        # sign-in and sign-out buttons and pack
        self.buttonSignIn = tk.Button(self.frameMain, height=13, width=55, text="Sign In", command=self.commandSignIn)
        self.buttonSignIn.pack()
        self.buttonSignOut = tk.Button(self.frameMain, height=13, width=55, text="Sign Out", command=self.commandSignOut)
        self.buttonSignOut.pack()

        # packs the main frame  to show the screen
        self.frameMain.pack()

        # Variable Declaration
        self.varSignIn = tk.StringVar(self.frameMain)       # stores Sign-in message
        self.varID = tk.StringVar(self.frameMain)           # Stores the input ID
        self.varName = tk.StringVar(self.frameMain)         # Stores the input Name
        self.varFinalName = tk.StringVar(self.frameMain)    # Stores finalized value of Name for submission
        self.varFinalID = tk.StringVar(self.frameMain)      # Stores finalized value of ID for submission

        # sets the default value for these variables (What you see in the entry boxes)
        self.varName.set("Name")
        self.varID.set("ID")
        self.varSignIn.set("Please swipe your student ID card")

    # Function called when sign-in button is pressed
    def commandSignIn(self):
        # hides the main class buttons
        self.frameMain.pack_forget()

        # opens the next window
        self.signinWindow = windowSignIn.windowSignIn(self)

    # Function called when the sign-out button is pressed
    def commandSignOut(self):
        # hide the main class buttons
        self.frameMain.pack_forget()

        # opens the sign-out window
        self.signoutWindow = windowSignOut.windowSignOut(self)

    # Function to load teacher/class array from server
    def loadClassTeachers(self):
        # Trys to load teachers if the server does not respond then repeat the call after 1 second
        try:
            self.arrayClassTeachers = client().getClassteacherArray()
        except UnboundLocalError as e:
            self.master.after(1000, self.loadClassTeachers)

    # used to prevent the 'x' button from doing anything
    def doNothing(self):
        pass



