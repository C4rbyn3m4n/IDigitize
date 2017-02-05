import tkinter as tk

import client as client
import dataStudent


class windowClassSelect():
    def __init__(self, parent):
        self.parent = parent

        self.frameClassSelect = tk.Frame(self.parent.parent.master)

        self.varDefaultClass = tk.StringVar(self.frameClassSelect)
        self.varDefaultClass.set("Classes")
        self.classes = self.getClasses()
        self.classes.append("OTHER")
        self.menuClasses = tk.OptionMenu(self.frameClassSelect, self.varDefaultClass, *self.classes,
                                         command=self.commandShowTeachers)
        self.menuClassesMenu = self.menuClasses.children["menu"]
        self.menuClasses.config(font=("Times New Roman", 40))
        self.menuClassesMenu.configure(font=("Arial", 40))
        self.menuClasses.pack()

        self.varDefaultTeacher = tk.StringVar(self.frameClassSelect)
        self.varDefaultTeacher.set("Teachers")
        self.teachers = self.getTeachers(self.varDefaultClass.get())
        self.menuTeachers = tk.OptionMenu(self.frameClassSelect, self.varDefaultTeacher, *self.teachers,
                                          command=self.commandSetTeacher)
        self.menuTeachersMenu = self.menuTeachers.children["menu"]
        self.menuTeachers.config(font=("Times New Roman", 40))
        self.menuTeachersMenu.config(font=("Times New Roman", 40))
        self.menuTeachers.pack()

        self.frameButtons = tk.Frame(self.frameClassSelect)
        tk.Button(self.frameButtons, text="Submit", command=self.commandSubmit).pack(side=tk.LEFT)
        tk.Button(self.frameButtons, text="Cancel", command=self.commandCancel).pack(side=tk.RIGHT)
        self.frameButtons.pack(side=tk.BOTTOM)
        self.parent.parent.master.bind('<Return>', lambda event: self.commandSubmit())

        self.frameClassSelect.pack()

    def commandShowTeachers(self, *name):
        self.varDefaultTeacher.set("Teachers")
        self.menuTeachersMenu.delete(0, "end")

        self.teachers = self.getTeachers(self.varDefaultClass.get())
        for teacher in self.teachers:
            self.menuTeachersMenu.add_command(label=teacher, command=lambda teach=teacher:
                                                                        self.varDefaultTeacher.set(teach))


    def commandSetTeacher(self, *vars):

        print(self.varDefaultTeacher.get())
        print(self.varDefaultClass.get())

    def getClasses(self):
        classes = []
        for Class in range(len(self.parent.parent.arrayClassTeachers)):
            classes.append(self.parent.parent.arrayClassTeachers[Class][0])
        return classes

    def getTeachers(self, selectedClass):
        print("Selcted Class: ", selectedClass)
        for i in self.parent.parent.arrayClassTeachers:
            if i[0] == selectedClass:
                teachers = []
                for j in range(1, len(i)):
                    teachers.append(i[j])
                teachers.append("OTHER")
                return teachers
        return ["Teachers", "OTHER"]

    def commandSubmit(self):
        if not self.varDefaultTeacher.get() == "Teachers" and not self.varDefaultClass.get() == "Classes":
            self.student = dataStudent.dataStudent(self.parent.parent.varFinalName.get(),
                                                   self.parent.parent.varFinalID.get(),
                                                   self.varDefaultClass.get(),
                                                   self.varDefaultTeacher.get())
            print(self.student)

            try:
                client.client().sendStudent(self.student)
                print("Student Sent!!")
            except Exception as e:
                print(e)
                print("Student failed to send!!")



            self.parent.parent.varName.set("Name")
            self.parent.parent.varID.set("ID")
            self.frameClassSelect.destroy()
            self.parent.parent.frameMain.pack()

    def commandCancel(self):
        self.parent.parent.master.bind('<Return>', self.commandDoNothing)
        self.frameClassSelect.destroy()
        self.parent.frameSignIn.pack()

    def commandDoNothing(self, *args):
        pass

