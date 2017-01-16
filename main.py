import tkinter as tk


class mainWindow():
    def __init__(self, master):
        self.master = master
        self.frameMain = tk.Frame(self.master)
        self.buttonSignIn = tk.Button(self.frameMain, height=13, width=55, text="Sign In", command=self.commandSignIn).pack()
        self.buttonSignOut = tk.Button(self.frameMain, height=13, width=55, text="Sign Out", command=self.commandSignOut).pack()

        self.frameMain.pack()

    def commandSignIn(self):
        pass

    def commandSignOut(self):
        while not cardSwipped():
            self.boxDisplay




if __name__ == '__main__':
    running = True

    root = tk.Tk()
    root.geometry("500x500")
    root.resizable(0, 0)
    window = mainWindow(root)
    root.title("Volunteer SignIn/SignOut")

    while running:
        root.update()
