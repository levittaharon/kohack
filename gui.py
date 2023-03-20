from tkinter import Tk, Toplevel
from tkinter.ttk import Label, Button
from tkinter import *
from tkinter import ttk 
import tkinter as tk
from tkinter.messagebox import showinfo

class Window:
    def __init__(self, master):
        self.master = master
 


        self.notebook = ttk.Notebook(self.master)
 
        # Frame 1 and 2
        self.frame1 = ttk.Frame(self.notebook)
        self.frame2 = ttk.Frame(self.notebook)
        self.label1 = ttk.Label(self.frame1, text = "")
        self.label1.pack(pady = 10, padx = 10)
        self.label2 = ttk.Label(self.frame2, text = "")
        self.label2.pack(pady = 10, padx = 10)

       
        self.frame1.pack(fill= tk.BOTH, expand=True)
        self.frame2.pack(fill= tk.BOTH, expand=True)
 
        self.notebook.add(self.frame1, text = "Bulk Orders")
        self.notebook.add(self.frame2, text = "Used Market")
 
        # Frame 3 and 4
        self.frame3 = ttk.Frame(self.notebook)
         
        self.label3 = ttk.Label(self.frame3, text = "")
        self.label3.pack(pady = 10, padx = 10)
         
        self.frame3.pack(fill= tk.BOTH, expand=True)
 
        self.notebook.insert("end", self.frame3, text = "Transportation")
        self.notebook.pack(padx = 5, pady = 5, expand = True)


         



 
root = tk.Tk()
window = Window(root)

#test

        


import tkinter as tk
import time

# --- functions ---

def on_ok():
    x, y = entry.get().split('x')
    for row in range(int(y)):
        for col in range(int(x)):
            print((col, row))

def tick():
    global time1

    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')

    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
    clock.after(200, tick)

# --- main window ---

time1 = ''


root.title('KoHack GUI')

# add frame in main window (root)

other = tk.Frame(root)
other.pack()

# put widgets in frame (other)

status = tk.Label(other, text="Skokie", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status.grid(row=10, column=10)

clock = tk.Label(other, font=('times', 20, 'bold'), bg='white')
clock.grid(row=0, column=1) 

# put other widget directly in main widnow (root)

tk.Label(root, text='GUI KoHack 2023 ').pack(side=tk.TOP, padx=100, pady=100)

entry = tk.Entry(root, width=25)
entry.pack(side=tk.TOP, padx=25, pady=25)

tk.Button(root, text='More info', command=on_ok).pack(side=tk.LEFT)
tk.Button(root, text='Quit', command=root.destroy).pack(side= tk.RIGHT)

tick()


 #scrolling 

# for scrolling vertically for frame1
yscrollbar = Scrollbar(window.frame1)
yscrollbar.pack(side = RIGHT, fill = Y)
  
label = Label(window.frame1,
              text = "Select Below",
              font = ("Times New Roman", 10), 
              padx = 10, pady = 10)
label.pack()
list = Listbox(window.frame1, selectmode = "multiple", 
               yscrollcommand = yscrollbar.set)
  
# Widget expands horizontally and 
# vertically by assigning both to
# fill option
list.pack(padx = 10, pady = 10,
          expand = YES, fill = "both")
  
x =['food', 'Cheese Pizza', 'Pinaple Pizza', 'Wraps']
  
for each_item in range(len(x)):
      
    list.insert(END, x[each_item])
    list.itemconfig(each_item, bg = "white")
  
# Attach listbox to vertical scrollbar
yscrollbar.config(command = list.yview)
#window.mainloop()



# for scrolling vertically for frame2
yscrollbar = Scrollbar(window.frame2)
yscrollbar.pack(side = RIGHT, fill = Y)
  
label = Label(window.frame2,
              text = "Select Below",
              font = ("Times New Roman", 10), 
              padx = 10, pady = 10)
label.pack()
list = Listbox(window.frame2, selectmode = "multiple", 
               yscrollcommand = yscrollbar.set)
  
# Widget expands horizontally and 
# vertically by assigning both to
# fill option
list.pack(padx = 10, pady = 10,
          expand = YES, fill = "both")
  
x =['Computers', 'Cars', 'Tablets', 'Phones']
  
for each_item in range(len(x)):
      
    list.insert(END, x[each_item])
    list.itemconfig(each_item, bg = "white")
  
# Attach listbox to vertical scrollbar
yscrollbar.config(command = list.yview)
#window.mainloop()






# for scrolling vertically for frame3
yscrollbar = Scrollbar(window.frame3)
yscrollbar.pack(side = RIGHT, fill = Y)
  
label = Label(window.frame3,
              text = "Select Below",
              font = ("Times New Roman", 10), 
              padx = 10, pady = 10)
label.pack()
list = Listbox(window.frame3, selectmode = "multiple", 
               yscrollcommand = yscrollbar.set)
  
# Widget expands horizontally and 
# vertically by assigning both to
# fill option
list.pack(padx = 10, pady = 10,
          expand = YES, fill = "both")
  
x =['food', 'freinds', 'places']
  
for each_item in range(len(x)):
      
    list.insert(END, x[each_item])
    list.itemconfig(each_item, bg = "white")
  
# Attach listbox to vertical scrollbar
yscrollbar.config(command = list.yview)
#window.mainloop()





#notebook in a notebook

def show():
    label.config( text = clicked.get() )
  
# Dropdown menu options
options = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7"
]
  
# datatype of menu text
clicked = StringVar()
  
# initial menu text
clicked.set( "Quanity" )
  
# Create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.pack()
  
# Create button, it will change label text
button = Button( root , text = "Order" , command = show ).pack()
  
# Create Label
label = Label( root , text = " " )
label.pack()
  






# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *
 
# creates a Tk() object
master = Tk()
 
# sets the geometry of main
# root window

 
 
# function to open a new window
# on a button click
def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(master)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("Student Info")
 
    # sets the geometry of toplevel
    
    # A Label widget to show in toplevel
    Label(newWindow,
          text ="This is a new window").pack()
 
 
label = Label(master,
              text ="This is the main window")
 
label.pack(pady = 10)
 
# a button widget which will open a
# new window on button click
btn = Button(master,
             text ="Click to open a new window",
             command = openNewWindow)
btn.pack(pady = 10)
 
# mainloop, runs infinitely
mainloop()



root.mainloop()