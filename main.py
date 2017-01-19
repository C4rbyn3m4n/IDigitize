# imports
import tkinter as tk
import mainWindow, windowClassSelect, windowSignIn, windowSignOut


if __name__ == '__main__':
    running = True

    root = tk.Tk()
    root.geometry("500x500")
    root.resizable(0, 0)
    window = mainWindow.mainWindow(root)
    root.title("Volunteer SignIn/SignOut")

    while running:
        root.update()
