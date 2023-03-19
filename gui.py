from tkinter import Tk, Toplevel
from tkinter.ttk import Label, Button
from tkinter import *
from tkinter import ttk 
import tkinter as tk
from tkinter.messagebox import showinfo
root = Tk()
root.title("Confirming Order")
root.geometry("500x500")

def new_window():
    top = Toplevel()
    top.title("Second window")
    top.geometry("400x500")    # By default, it is kept as the geometry of the main window, but you can change it.
    lab = Label(top, text="order is in!")
    lab.pack(pady=20)

l = Label(root, text="tap confirm for order to go through")
l.pack(pady=20)

b = Button(root, text="Confirm", command=new_window)
b.pack(pady=50)


class Window:
    def __init__(self, master):
        self.master = master
 
        self.notebook = ttk.Notebook(self.master)
 
        # Frame 1 and 2
        self.frame1 = ttk.Frame(self.notebook)
        self.frame2 = ttk.Frame(self.notebook)
 
        self.label1 = ttk.Label(self.frame1, text = "Invetory,  Items left in stock, price $5")
        self.label1.pack(pady = 20, padx = 10)
        self.label2 = ttk.Label(self.frame2, text = "Item 3:3 left in stock")
        self.label2.pack(pady = 15, padx = 10)
 
        self.frame1.pack(fill= tk.BOTH, expand=True)
        self.frame2.pack(fill= tk.BOTH, expand=True)
 
        self.notebook.add(self.frame1, text = "Bulk Orders")
        self.notebook.add(self.frame2, text = "Used Market")
 
        # Frame 3
        self.frame3 = ttk.Frame(self.notebook)
         
        self.label3 = ttk.Label(self.frame3, text = "praying with fire, Gemera sukkah")
        self.label3.pack(pady = 50, padx = 20)
         
        self.frame3.pack(fill= tk.BOTH, expand=True)
 
        self.notebook.insert("end", self.frame3, text = "Transportation")
        self.notebook.pack(padx = 5, pady = 5, expand = True)
         
 
root = tk.Tk()
window = Window(root)


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

clock = tk.Label(other, font=('times', 20, 'bold'), bg='green')
clock.grid(row=0, column=1) 

# put other widget directly in main widnow (root)

tk.Label(root, text='GUI KoHack 2023 ').pack(side=tk.TOP, padx=100, pady=100)

entry = tk.Entry(root, width=25)
entry.pack(side=tk.TOP, padx=25, pady=25)

tk.Button(root, text='More info', command=on_ok).pack(side=tk.LEFT)
tk.Button(root, text='Join', command=root.destroy).pack(side= tk.RIGHT)

tick()


  

# scrolling

  
#window.title('Multiple selection')
  
# for scrolling vertically
yscrollbar = Scrollbar(window.frame1)
yscrollbar.pack(side = RIGHT, fill = Y)
  
label = Label(window.frame1,
              text = "Select the languages below :  ",
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
  
x =['food', 'freinds', 'places']
  
for each_item in range(len(x)):
      
    list.insert(END, x[each_item])
    list.itemconfig(each_item, bg = "lime")
  
# Attach listbox to vertical scrollbar
yscrollbar.config(command = list.yview)
#window.mainloop()

# --- start ---












root.mainloop()