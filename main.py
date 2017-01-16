import tkinter as tk


class mainWindow():
    def __init__(self, master):
        self.master = master
        self.frameMain = tk.Frame(self.master)
        self.buttonSignIn = tk.Button(self.frameMain, height=13, width=55, text="Sign In", command=self.commandSignIn)
        self.buttonSignIn.pack()
        self.buttonSignOut = tk.Button(self.frameMain, height=13, width=55, text="Sign Out", command=self.commandSignOut)
        self.buttonSignOut.pack()

        self.frameMain.pack()

    def commandSignIn(self):
        pass

    def commandSignOut(self):
        self.varName = tk.StringVar(self.frameMain)
        self.varName.set("Name")
        self.varID = tk.StringVar(self.frameMain)
        self.varID.set("ID")
        self.varSignIn = tk.StringVar(self.frameMain)
        self.varSignIn.set("Please swipe your student ID card")
        self.frameMain.pack_forget()

        self.frameSignOut = tk.Frame(self.master)
        tk.Label(self.frameSignOut, text=self.varSignIn.get()).pack()
        tk.Entry(self.frameSignOut, text=self.varName, justify="center").pack()
        tk.Entry(self.frameSignOut, text=self.varID, justify="center").pack()
        self.frameSignOutButtons = tk.Frame(self.frameSignOut)
        tk.Button(self.frameSignOutButtons, text="Submit", command=self.commandSubmit).pack(side=tk.LEFT)
        tk.Button(self.frameSignOutButtons, text="Cancel", command=self.commandCancel).pack(side=tk.RIGHT)
        self.frameSignOutButtons.pack()
        self.frameSignOut.pack()

        while not self.getSwipe():
            pass
        # self.varName.set(self.nameScanned)
        # self.varID.set(self.IDScanned)

    def commandSubmit(self):
        pass

    def commandCancel(self):
        self.frameSignOut.destroy()
        self.frameMain.pack()


    def getSwipe(self):
        # while not self.test:
        #     pass
        return True






if __name__ == '__main__':
    running = True

    root = tk.Tk()
    root.geometry("500x500")
    root.resizable(0, 0)
    window = mainWindow(root)
    root.title("Volunteer SignIn/SignOut")

    while running:
        root.update()
