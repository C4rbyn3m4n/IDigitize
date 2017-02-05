# imports
import tkinter as tk
import windowMain

# checks to make sure this is note called as an import
if __name__ == '__main__':
    # make main window
    root = tk.Tk()

    # make it non-resizable
    root.resizable(0, 0)

    # opens the main window as a class
    window = windowMain.windowMain(root)
    # sets title of window
    root.title("Volunteer SignIn/SignOut")

    # starts the mainloop of the window
    root.mainloop()
