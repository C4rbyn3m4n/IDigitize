# imports
import tkinter as tk

from MainClass import windowMain

if __name__ == '__main__':
    running = True

    root = tk.Tk()
    root.resizable(0, 0)
    window = windowMain.windowMain(root)
    root.title("Volunteer SignIn/SignOut")

    root.mainloop()
