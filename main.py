# imports
import tkinter as tk
import windowMain


if __name__ == '__main__':
    running = True

    root = tk.Tk()
    root.geometry("500x500")
    root.resizable(0, 0)
    window = windowMain.mainWindow(root)
    root.title("Volunteer SignIn/SignOut")

    while running:
        root.update()
