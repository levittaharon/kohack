import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Banana Interest Survey")
root.geometry("640x480+300+300")#size, position
root.resizable(False, False)#horizontally, vertically
mylabel = ttk.Label(root, text="this is a label")
mysecondlabel = ttk.Label(root, text="this is my second label")
mylabel.grid(row=1, column=0, stick=tk.W)
mysecondlabel.grid(row=2,column = 0, sticky=tk.W)
mystring_var = 0
myentry=ttk.Entry(root,textvariable=mystring_var, width=20)
myentry.grid(row=1, column=3, columnspan=2)
myspinbox= ttk.Spinbox(root, from_=0, to=100, increment=0.1)
myspinbox.grid(row=1,column=3)
mycheckbutton = ttk.Checkbutton(
    root, text="john")
mycheckbutton.grid(row=2, column=1)
buttons = tk.Frame(root)
rd= False
r1 = ttk.Radiobutton(buttons, variable = rd, value=1, text="one")
r2 = ttk.Radiobutton(buttons, variable = rd, value=2, text="two")
buttons.grid(row=3, column=1)
r1.grid(row=1, column=1)
r2.grid(row=2, column=1)
mycombo = ttk.Combobox(root,values=["This option", "that option", "another option"])
mycombo.grid(row=4, column=1)
mytext = tk.Text(root, undo=True, maxundo=100, spacing1=10, spacing2=2, spacing3=5, height=5, width=30, wrap='word')
mytext.insert("1.0", "text widgets are awesome")
def john():
    print(mytext.get("1.0", tk.END))
mytext.grid(row=3, column=0)
mybutton = ttk.Button(root, command=john, text="Click me!", default="active")
mybutton.grid(row=4, column=0)
mylabelframe=ttk.LabelFrame(root,text="Button frame")
b1=ttk.Button(mylabelframe, text="button1")
b2=ttk.Button(mylabelframe, text="button2")
b1.pack()
b2.pack()
mylabelframe.grid(row=5, column =0)
root.mainloop()
