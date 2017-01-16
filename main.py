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
        self.nameVar = tk.StringVar(self.frameMain)
        self.nameVar.set("Name")
        self.IDVar = tk.StringVar(self.frameMain)
        self.IDVar.set("ID")
        self.buttonSignIn.destroy()
        self.buttonSignOut.destroy()

        self.frameSignOut = tk.Frame(self.frameMain)
        tk.Label(self.frameSignOut, text="Please swipe your student ID").pack()
        tk.Entry(self.frameSignOut, text=self.nameVar, justify="center").pack()
        tk.Entry(self.frameSignOut, text=self.IDVar, justify="center").pack()
        self.frameSignOutButtons = tk.Frame(self.frameSignOut)
        tk.Button(self.frameSignOutButtons, text="Submit", command=self.commandSubmit).pack(side=tk.LEFT)
        tk.Button(self.frameSignOutButtons, text="Cancel", command=self.commandCancel).pack(side=tk.RIGHT)
        self.frameSignOutButtons.pack()
        self.frameSignOut.pack()

        while not self.getSwipe():
            pass
        # self.nameVar.set(self.nameScanned)
        # self.IDVar.set(self.IDScanned)

    def commandSubmit(self):
        pass

    def commandCancel(self):
        pass

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
