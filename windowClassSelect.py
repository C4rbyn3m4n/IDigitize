import tkinter as tk

class windowClassSelect():
    def __init__(self, parent):
        self.parent = parent

        self.frameClassSelect = tk.Frame(self.parent.parent.master)

        self.varDefaultClass = tk.StringVar(self.frameClassSelect)
        self.varDefaultClass.set("Classes")
        self.classes = self.getClasses()
        self.menuClasses = tk.OptionMenu(self.frameClassSelect, self.varDefaultClass, *self.classes, command=self.commandShowTeachers)
        self.menuClassesMenu = self.menuClasses.children["menu"]
        self.menuClasses.config(font=("Times New Roman", 40))
        self.menuClassesMenu.configure(font=("Arial", 40))
        self.menuClasses.pack()

        self.varDefaultTeacher = tk.StringVar(self.frameClassSelect)
        self.varDefaultTeacher.set("Teachers")
        self.teachers = self.getTeachers(self.varDefaultClass.get())
        self.menuTeachers = tk.OptionMenu(self.frameClassSelect, self.varDefaultTeacher, *self.teachers, command=self.commandSetTeacher)
        self.menuTeachersMenu = self.menuTeachers.children["menu"]
        self.menuTeachers.config(font=("Times New Roman", 40))
        self.menuTeachersMenu.config(font=("Times New Roman", 40))
        self.menuTeachers.pack()

        self.frameClassSelect.pack()

    def commandShowTeachers(self, *name):
        self.varDefaultTeacher.set("Teachers")
        self.menuTeachersMenu.delete(0, "end")

        self.teachers = self.getTeachers(self.varDefaultClass.get())
        for teacher in self.teachers:
            self.menuTeachersMenu.add_command(label=teacher, command=lambda teach=teacher: self.varDefaultTeacher.set(teach))


    def commandSetTeacher(self, *vars):

        print(self.varDefaultTeacher.get())
        print(self.varDefaultClass.get())

    def getClasses(self):
        return ["Calc", "English", "Science"]

    def getTeachers(self, selectedClass):
        print("Selcted Class: ", selectedClass)
        if selectedClass == "Classes":
            return ["-----"]
        elif selectedClass == "Calc":
            return ["Calc Teacher 1", "Calc Teacher 2"]
        elif selectedClass == "English":
            return ["English Teacher 1", "English Teacher 2"]
        elif selectedClass == "Science":
            return ["Science Teacher 1", "Science Teacher 2"]
        else:
            return ["one", "two"]

