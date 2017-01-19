import tkinter as tk

class windowListenMain():
    def __init__(self, parent):
        self.parent = parent

        self.frameMain = tk.Frame(parent)
        tk.Label(self.frameMain, text="test").pack()

        self.frameMain.pack()
