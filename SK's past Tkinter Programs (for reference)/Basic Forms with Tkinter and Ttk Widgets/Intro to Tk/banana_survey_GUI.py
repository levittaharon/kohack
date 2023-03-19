import tkinter as tk
root = tk.Tk()
root.title("Banana Interest Survey")
root.geometry("640x480+300+300")#size, position
root.resizable(False, False)#horizontally, vertically
title = tk.Label(root, text="Please Take Survey", font=("Arial 16 bold"), bg="brown", fg="#FF0")
name_var = tk.StringVar(root)
name_label= tk.Label(root, text="What is your name")
name_inp = tk.Entry(root, textvariable=name_var)
eater_var = tk.BooleanVar()
eater_inp = tk.Checkbutton(root, variable = eater_var, text="Eat bananas")
num_var = tk.IntVar(value=3)
num_label = tk.Label(root, text="How many bananas do you eat per day?")
num_inp = tk.Spinbox(root, from_=0, to=1000, increment=1, textvariable=num_var)
color_var = tk.StringVar(value="any")
color_label = tk.Label(root, text="What is the best color of a banana?")
#color_inp = tk.Listbox(root, height=1)
color_choices = ("any", "green", "brown", "black", "yellow")
color_inp = tk.OptionMenu(
    root, color_var, *color_choices)
#for choice in color_choices:
#    color_inp.insert(tk.END, choice)
orange_var = tk.BooleanVar()
orange_label = tk.Label(root, text="Do you eat oranges?")
orange_frame = tk.Frame(root)
orange_yes_inp = tk.Radiobutton(orange_frame, text = "yes", value=True, variable=orange_var)
orange_no_inp = tk.Radiobutton(orange_frame, text="No", value=False, variable=orange_var)
info = tk.Label(root, text="Write a memo about your favourite banana experience")
info_inp = tk.Text(root, height = 3)
submit_btn = tk.Button(root, text="Submit Survey")
output_var = tk.StringVar(value="")
output_line = tk.Label(root, textvariable = output_var, text="", anchor="w", justify="left")#west/left, justify(individ lines of text)
title.grid(columnspan=2)#both grid() and pack()-sequential order and place()-specific pixel are geometry manager methods
name_label.grid(row=1, column=0)
name_inp.grid(row=1, column=1)
eater_inp.grid(row = 2, columnspan=2, sticky=(tk.W + tk.E))#West and East
num_label.grid(row=3, sticky=tk.W)
num_inp.grid(row=3, column=1, sticky=(tk.W+tk.E))
color_label.grid(row=4, columnspan=2, sticky=tk.W, pady=10)#pady and padx outer padding, ipady and ipadx inner padding
color_inp.grid(row=5, columnspan=2, sticky=tk.W+tk.E, padx=25)
orange_yes_inp.pack(side="left", fill="x", ipadx=10, ipady=5)
orange_no_inp.pack(side="left", fill="x", ipadx=10, ipady=5)
orange_label.grid(row=6, columnspan=2, sticky=tk.W)
orange_frame.grid(row=7, columnspan=2, stick=tk.W)
info.grid(row=8, sticky = tk.W)
info_inp.grid(row=9, columnspan=2, sticky = "NSEW")
submit_btn.grid(row=99)
output_line.grid(row=100, columnspan=2, sticky="NSEW")
root.columnconfigure(1, weight=1)
root.rowconfigure(99, weight = 2)
root.rowconfigure(100, weight=1)
# def sub():
#         name=name_inp.get()
#         number=num_inp.get()
#         selected_idx=color_inp.curselection()
#         if selected_idx:
#             color=color_inp.get(selected_idx)
#         else:
#             color=""
#         infop = info_inp.get("1.0", tk.END)
#         message = (f"Thnks for taking the survey, {name}. \n Enjoy your {number} {color} bananas.")
#         output_line.configure(text=message)
#         print(infop)
def sub():
    name = name_var.get()
    try:
        number = num_var.get()
    except tk.TclError:
        number = 10000
    color = color_var.get()
    banana_eater=eater_var.get()
    orange_eater = orange_var.get()
    infop = info_inp.get("1.0", tk.END)
    message = f"Thanks for taking the survey, {name}. \n"
    if not banana_eater:
        message+=f"Sorry you dont like bananas.\n"
    else:
        message+=f"Enjoy your {number} {color} bananas.\n"
    if orange_eater:
        message+=f"Enjoy your oranges!\n"
    else:
        message+=f"Avoid Oranges.\n"
    if infop.strip():
        message+=f"Your Info: {infop}\n"
    output_var.set(message)
submit_btn.configure(command=sub)
print(name_var.get())
root.mainloop()
