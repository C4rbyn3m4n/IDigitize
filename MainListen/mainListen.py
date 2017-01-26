import tkinter as tk
from MainListen.windowListenMain import windowListenMain

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x600")
    mainWindow = windowListenMain(root)

    while 1:
        root.update_idletasks()
        root.update()