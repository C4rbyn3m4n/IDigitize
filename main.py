# imports
import tkinter as tk

class mainWindow():
    def __init__(self, master):
        self.master = master

        # create sign-in and sign-out buttons
        self.frameMain = tk.Frame(self.master)
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

        self.signinWindow = windowSignIn(self)

    def commandSignOut(self):
        # set up variables for the Sign out window

        # hide the main class buttons
        self.frameMain.pack_forget()

        self.signoutWindow = windowSignOut(self)

    def readCardData(self, cardInfo):
        #self.swipe.destroy()
        # TODO: Readcard data
        print(cardInfo)
        self.CardLabel.config(text="Error")

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
        self.CardLabel=tk.Label(self.mframe, text="Scan your card")
        self.CardLabel.pack()
        self.mEntry = tk.Entry(self.mframe, text=self.var)
        self.mEntry.pack()
        self.mEntry.focus()

        self.frameButtons= tk.Frame(self.mframe)
        self.buttonOkay = tk.Button(self.frameButtons, text="OK", command=lambda: self.readCardData(self.var.get()))
        self.buttonOkay.pack(side=tk.LEFT)
        self.swipe.bind('<Return>', lambda event: self.readCardData(self.var.get()))

        tk.Button(self.frameButtons, text="Camcel", command=lambda: self.swipe.destroy()).pack(side=tk.RIGHT)

        self.frameButtons.pack()
        self.mframe.pack()
        self.swipe.mainloop()

        return True


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
        self.frameSignOutButtons.pack()
        self.frameSignOut.pack()

        while not self.parent.getSwipe():
            pass
        # self.varName.set(self.nameScanned)
        # self.varID.set(self.IDScanned)

    def commandSubmit(self):
        self.parent.varFinalID.set(self.parent.varID.get())
        self.parent.varFinalName.set(self.parent.varName.get())

        # the rest of the sign out code goes here
        #
        #
        #

    def commandCancel(self):
        # clear final variables
        self.parent.varFinalID.set("")
        self.parent.varFinalName.set("")

        self.frameSignOut.destroy()
        self.parent.frameMain.pack()



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
        self.frameSignInButtons.pack()
        self.frameSignIn.pack()

        while not self.parent.getSwipe():
            pass

    def commandSubmit(self):
        self.parent.varFinalID.set(self.parent.varID.get())
        self.parent.varFinalName.set(self.parent.varName.get())

        print(self.parent.varFinalID.get())
        print(self.parent.varFinalName.get())

        self.frameSignIn.pack_forget()
        self.selectTeacherWindow = windowClassSelect(self)


    def commandCancel(self):
        # Clear final variables
        self.parent.varFinalID.set("")
        self.parent.varFinalName.set("")
        self.frameSignIn.destroy()
        self.parent.frameMain.pack()

class windowClassSelect():
    def __init__(self, parent):
        self.parent = parent

        self.frameClassSelect = tk.Frame(self.parent.parent.master)

        self.varDefaultClass = tk.StringVar(self.frameClassSelect)
        self.varDefaultClass.set("Classes")
        self.classes = self.getClasses()
        self.menuClasses = tk.OptionMenu(self.frameClassSelect, self.varDefaultClass, *self.classes, command=self.commandShowTeachers)
        self.menuClassesMenu = self.menuClasses.children["menu"]
        self.menuClasses.config(font=("Times New Roman", 40))
        # self.menuClasses.children["button"].configure(font=("arial", 40))
        self.menuClassesMenu.configure(font=("Arial", 40))
        self.menuClasses.pack()

        self.varDefaultTeacher = tk.StringVar(self.frameClassSelect)
        self.varDefaultTeacher.set("Teachers")
        self.teachers = self.getTeachers(self.varDefaultClass.get())
        self.menuTeachers = tk.OptionMenu(self.frameClassSelect, self.varDefaultTeacher, *self.teachers, command=self.commandSetTeacher)
        self.menuTeachers.config(font=("Times New Roman", 40))
        self.menuTeachersMenu = self.menuTeachers.children["menu"]
        self.menuTeachersMenu.config(font=("Times New Roman", 40))
        self.menuTeachers.pack()

        self.frameClassSelect.pack()

    def commandShowTeachers(self, *name):

        self.menuTeachersMenu.delete(0, "end")
        self.teachers = self.getTeachers(self.varDefaultClass.get())
        for teacher in self.teachers:
            self.menuTeachersMenu.add_command(label=teacher, command=self.commandShowTeachers)

    def commandSetTeacher(self, *vars):
        print(self.varDefaultTeacher.get())
        print(self.varDefaultClass.get())

    def getClasses(self):
        return ["Calc", "English", "Science"]

    def getTeachers(self, selectedClass):
        print("Selcted Class: ", selectedClass)
        if selectedClass == "Classes":
            return ["-----"]
        elif selectedClass == "Calc":
            return ["Calc Teacher 1", "Calc Teacher 2"]
        elif selectedClass == "English":
            return ["English Teacher 1", "English Teacher 2"]
        elif selectedClass == "Science":
            return ["Science Teacher 1", "Science Teacher 2"]
        else:
            return ["one", "two"]





if __name__ == '__main__':
    running = True

    root = tk.Tk()
    root.geometry("500x500")
    root.resizable(0, 0)
    window = mainWindow(root)
    root.title("Volunteer SignIn/SignOut")

    while running:
        root.update()
