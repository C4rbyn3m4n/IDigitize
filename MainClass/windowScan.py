import tkinter as tk

class windowScan():
    def __init__(self, parent):
        self.parent = parent
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
        self.CardLabel = tk.Label(self.mframe, text="Scan your card")
        self.CardLabel.pack()

        self.frameButtons = tk.Frame(self.mframe)
        self.buttonOkay = tk.Button(self.frameButtons, text="OK", command=self.okay, height=3, width=10)
        self.buttonOkay.pack(side=tk.LEFT)
        self.swipe.bind('<Return>', lambda event: self.okay())
        self.frameButtons.pack()

        tk.Button(self.frameButtons, text="Cancel",height=3, width=10, command=lambda: self.swipe.destroy()).pack(side=tk.RIGHT)

        self.mEntry = tk.Entry(self.mframe, text=self.var)
        self.mEntry.pack()
        self.mEntry.focus()

        self.mframe.pack()
        self.swipe.mainloop()

    def okay(self):
        self.parent.readCard(self.var.get())
        self.swipe.destroy()
