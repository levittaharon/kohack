import tkinter as tk
from tkinter import ttk
print("John")
root = tk.Tk()
root.title("Gradebook +")
root.columnconfigure(0, weight=1)#Only one column is set, but ensures that form stays centred when expanding
variables = dict()
variables["Student"]=tk.StringVar()
variables["Subject"]=tk.StringVar()
variables["Assignment Name"]=tk.StringVar()
variables["Assignment Weight"]=tk.StringVar()
variables["Assignment Grade"]=tk.StringVar()
class LabelInput(tk.Frame):
    def __init__(
        self, parent, label, inp_cls, inp_args, *args, **kwargs
    ):
        super().__init__(parent, *args, **kwargs)
        self.label = tk.Label(self, text=label, anchor="w")
        self.input = inp_cls(self, **inp_args)
        self.columnconfigure(1, weight=1)
        self.label.grid(sticky=tk.E + tk.W)
        self.input.grid(row=0, column=1, sticky=tk.E + tk.W)
class Pupil():
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.Assignments = {"History Final":{"Weight":5, "Grade":75}, "Washington Essay":{"Weight":2, "Grade":65}}
        self.GPA = 0
        self.Report_Frame = tk.Frame(root)
        self.Report_Frame.grid()
    def GPA_calc(self):    
        self.assign=0
        GPAA = 0
        for i in self.Assignments:
            self.assign +=self.Assignments[i]["Weight"]
            GPAA += self.Assignments[i]["Weight"]*self.Assignments[i]["Grade"]
        self.GPA = str(GPAA/self.assign)
        return self.GPA
    def Load_Report(self):
        self.details = ""
        for Assignment in self.Assignments:
            self.details += ("\n" + Assignment + " Score: " + str(self.Assignments[Assignment]["Grade"]))
        report_text = self.subject + " Overall Grade: " + self.GPA_calc() +"\n" + (self.details)
        self.Subject_Report = tk.Label(self.Report_Frame, text=report_text)
        self.Subject_Report.grid(column=2, row=2, sticky=(tk.W + tk.E))
    def Assign_operations(self, arg):
        self.Record_Assignment_Frame = tk.Frame(root)
        self.Record_Assignment_Frame.grid(row=1, column=0)
        self.Assignment_Name=LabelInput(self.Record_Assignment_Frame, "Enter Assignment Name", ttk.Entry, {"textvariable":variables["Assignment Name"]})
        def Delete_Assignment():
            self.label= tk.Label(self.Record_Assignment_Frame, text="DELETE ASSIGNMENT")
            self.label.grid()
            self.Assignment_Name.grid()
            self.Confirm_del = tk.Button(root, text="Confirm Assignment", command=lambda: self.Confirmdel())
            self.Confirm_del.grid(row=3)
        def Record_Assignment():
            self.label = tk.Label(self.Record_Assignment_Frame, text="NEW ASSIGNMENT")
            self.label.grid()
            self.Assignment_Weight = LabelInput(self.Record_Assignment_Frame, "Enter Weight of Assignment", ttk.Entry, {"textvariable":variables["Assignment Weight"]})
            self.Assignment_Grade = LabelInput(self.Record_Assignment_Frame, "Enter Percentage Score", ttk.Entry, {"textvariable":variables["Assignment Grade"]})
            self.Assignment_Name.grid()
            self.Assignment_Grade.grid()
            self.Assignment_Weight.grid()
            self.Confirm_add = tk.Button(root, text="Confirm Assignment", command=lambda: self.Confirmadd())
            self.Confirm_add.grid(row=3)
        if arg=="del":
            Delete_Assignment()
        elif arg=="rec":
            Record_Assignment()
    def Confirmadd(self):
            print(self.Assignment_Grade, self.Assignment_Name, self.Assignment_Weight)
            self.Assignments[self.Assignment_Name.input.get()] = {"Weight":int(self.Assignment_Weight.input.get()), "Grade":int(self.Assignment_Grade.input.get())}
            self.Subject_Report.grid_remove()
            self.Load_Report()
            self.Confirm_add.grid_remove()
            self.Assignment_Name.grid_remove()
            self.Assignment_Grade.grid_remove()
            self.Assignment_Weight.grid_remove()
            self.label.grid_remove()
    def Confirmdel(self):
         del self.Assignments[self.Assignment_Name.input.get()]
         self.Subject_Report.grid_remove()
         self.Load_Report()
         self.Confirm_del.grid_remove()
         self.Assignment_Name.grid_remove()
         self.Assignment_Grade.grid_remove()
         self.Assignment_Weight.grid_remove()
         self.label.grid_remove()

student_directory = {"Honors Biology": ["John", "Bob"], "Nuclear Physics":["Simon", "Fred", "Larry", "Joe"]}
student_repository = {}
for key, value in student_directory.items():
    for l in value:
        student_repository[l] = Pupil(l, key)
student_directory_set = {*list(student_repository.keys())}
print(student_directory_set)
def Action(e):
    Students.input.config(value=student_directory[Subject.input.get()])
    Students.input.current(0)
selected = False
    

Subject = LabelInput(root, "Select Subject: ", ttk.Combobox, {"textvariable":variables["Subject"], "value":list(student_directory.keys())})
Subject.input.bind("<<ComboboxSelected>>", Action)
Students = LabelInput(root, "Select Student: ", ttk.Combobox, {"textvariable":variables["Student"], "value":[]})
Subject.grid()
Students.grid()
Load_Button = tk.Button(root, text="Load Student Report", command= lambda: student_repository[Students.input.get()].Load_Report())
Load_Button.grid()
Add_Button = tk.Button(root, text="Record Assignment", command=lambda: student_repository[Students.input.get()].Assign_operations("rec"))
Del_Button = tk.Button(root, text="Delete Assignment", command=lambda: student_repository[Students.input.get()].Assign_operations("del"))
Load_Button.grid()
Add_Button.grid()
Del_Button.grid()
Message_Log = LabelInput
root.mainloop()